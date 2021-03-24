import os
import shutil

from pyengine.common.utils import build_logger as logger
from pyengine.build.component_builder import ComponentBuilder


class ProjectBuilder:
    build_folders = {
        "objects": os.path.join("pyengine", "build", "objects"),
        "components": os.path.join("pyengine", "build", "objects", "components"),
        "scripts": os.path.join("pyengine", "build", "objects", "scripts"),
        "templates": os.path.join("pyengine", "build", "templates")
    }
    project_folders = {}

    @staticmethod
    def generate_component(text, comp):
        logger.info("GENERATE COMPONENT : "+comp.name)
        if comp.name == "TransformComponent":
            return ComponentBuilder.generate_transform_component(text, comp)
        elif comp.name == "SpriteComponent":
            return ComponentBuilder.generate_sprite_component(text, comp)
        elif comp.name == "TextComponent":
            return ComponentBuilder.generate_text_component(text, comp)
        elif comp.name == "CollisionComponent":
            return ComponentBuilder.generate_collision_component(text, comp)
        elif comp.name == "BasicPhysicComponent":
            return ComponentBuilder.generate_basicphysic_component(text, comp)
        elif comp.name == "ControlComponent":
            return ComponentBuilder.generate_control_component(text, comp)
        elif comp.name == "SpriteSheetComponent":
            return ComponentBuilder.generate_spritesheet_component(text, comp)
        elif comp.name.startswith("ScriptComponent"):
            return ComponentBuilder.generate_script_component(text, comp, ProjectBuilder.project_folders["scripts"])
        else:
            return text

    @staticmethod
    def generate_gameobject(text, gameobject):
        logger.info("GENERATE GAMEOBJECT : "+gameobject.name)
        replaces = {
            "{NAME}": str(gameobject.name)
        }
        with open(os.path.join(ProjectBuilder.build_folders["templates"], "gameobject.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        # GENERATE COMPONENTS
        for i in gameobject.components:
            template = ProjectBuilder.generate_component(template, i)
            if i.name.startswith("ScriptComponent"):
                template = template.replace(
                    "{COMPONENTS}",
                    f"    {gameobject.name}.add_component({i.name.split(' ')[-1].lower()})\n" + "{COMPONENTS}"
                )
            else:
                template = template.replace(
                    "{COMPONENTS}",
                    f"    {gameobject.name}.add_component({i.name.split(' ')[-1].lower()})\n" + "{COMPONENTS}"
                )
        template += "\n"
        template = template.replace("{COMPONENTS}\n", "")

        # GENERATE CHILDS
        for i in gameobject.childs:
            template = ProjectBuilder.generate_gameobject(template, i)
            template += f"    {gameobject.name}.childs.append({i.name})\n"
        template = template.replace("{CHILDS}\n", "")

        return text.replace("{ENTITIES}", template)

    @staticmethod
    def generate_scene(text, scene):
        logger.info("GENERATE SCENE : "+scene.name)
        replaces = {
            "{NAME}": str(scene.name),
            "{COLOR}": str(scene.components[0].color),
            "{ENTITIES_NAMES}": str([i.name for i in scene.childs]).replace("'", "")
        }
        with open(os.path.join(ProjectBuilder.build_folders["templates"], "scene.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        # GENERATE ENTITIES
        for i in scene.childs:
            template = ProjectBuilder.generate_gameobject(template, i)
        template = template.replace("{ENTITIES}\n", "")

        return text.replace("{SCENES}", template)

    @staticmethod
    def generate_main(path, project):
        replaces = {
            "{NAME}": str(project.name),
            "{WIDTH}": str(project.settings.get("width", 1280)),
            "{HEIGHT}": str(project.settings.get("height", 720)),
            "{SCENES_NAMES}": str([i.name for i in project.scenes]).replace("'", "")
        }
        with open(os.path.join(ProjectBuilder.build_folders["templates"], "main.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        # GENERATE SCENES
        for i in project.scenes:
            template = ProjectBuilder.generate_scene(template, i)
        template = template.replace("{SCENES}", "")

        with open(path, "w") as f:
            f.write(template)

    @staticmethod
    def build(project):
        logger.info("BUILD : STARTED")
        ProjectBuilder.project_folders = {
            "main": os.path.join("builds", project.name),
            "files": os.path.join("builds", project.name, "files"),
            "components": os.path.join("builds", project.name, "files", "components"),
            "scripts": os.path.join("builds", project.name, "files", "scripts"),
            "resources": os.path.join("builds", project.name, "resources")
        }
        shutil.rmtree(os.path.join("builds", project.name), ignore_errors=True)
        for i in ProjectBuilder.project_folders.values():
            logger.info("CREATE DIR : " + i)
            os.makedirs(i, exist_ok=True)

        logger.info("COPY CORE FILES : STARTED")
        for i in os.listdir(ProjectBuilder.build_folders["objects"]):
            if i != "components" and i != "scripts":
                logger.info("CORE FILE : " + i)
                shutil.copyfile(
                    os.path.join(ProjectBuilder.build_folders["objects"], i),
                    os.path.join(ProjectBuilder.project_folders["files"], i)
                )
        for i in os.listdir(ProjectBuilder.build_folders["components"]):
            logger.info("CORE COMPONENT FILE : " + i)
            shutil.copyfile(
                os.path.join(ProjectBuilder.build_folders["components"], i),
                os.path.join(ProjectBuilder.project_folders["components"], i)
            )
        for i in os.listdir(ProjectBuilder.build_folders["scripts"]):
            logger.info("CORE SCRIPT FILE : " + i)
            shutil.copyfile(
                os.path.join(ProjectBuilder.build_folders["scripts"], i),
                os.path.join(ProjectBuilder.project_folders["scripts"], i)
            )
        logger.info("COPY CORE FILES : SUCCESSFULLY ENDED")

        logger.info("COPY GAME RESOURCES : STARTED")
        for i in project.textures:
            logger.info("GAME RESOURCE : " + i.components[0].path)
            ext = i.components[0].path.split(".")[-1]
            ComponentBuilder.sprites[i.name] = ext
            shutil.copyfile(
                i.components[0].path,
                os.path.join(ProjectBuilder.project_folders["resources"], i.name+"."+ext)
            )
        logger.info("COPY GAME RESOURCES : SUCCESSFULLY ENDED")

        logger.info("COPY GAME SCRIPTS : STARTED")
        for i in os.listdir(project.folders["scripts"]):
            logger.info("GAME SCRIPT : "+i)
            shutil.copyfile(
                os.path.join(project.folders["scripts"], i),
                os.path.join(ProjectBuilder.project_folders["scripts"], i)
            )

        logger.info("COPY GAME SCRIPT : SUCCESSFULLY ENDED")

        logger.info("GENERATE GAME FILES : STARTED")
        logger.info("GENERATE : Main")
        ProjectBuilder.generate_main(
            os.path.join(ProjectBuilder.project_folders["main"], project.name.title()+".py"),
            project
        )
        logger.info("GENERATE GAME FILES : SUCCESSFULLY ENDED")

        logger.info("BUILD : SUCCESSFULLY ENDED")
