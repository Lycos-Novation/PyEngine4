import os
import shutil

from pyengine.common.utils import build_logger as logger
from pyengine.build.component_builder import ComponentBuilder


class ProjectBuilder:
    build_folders = {
        "objects": os.path.join("pyengine", "build", "objects"),
        "components": os.path.join("pyengine", "build", "objects", "components"),
        "scripts": os.path.join("pyengine", "build", "objects", "scripts"),
        "templates": os.path.join("pyengine", "build", "templates"),
        "utils": os.path.join("pyengine", "common", "utils")
    }
    project_folders = {}
    components = {}

    @staticmethod
    def generate_component(text, comp):
        logger.info("GENERATE COMPONENT : "+comp.name)
        if not comp.name.startswith("Script"):
            ProjectBuilder.components[comp.name] = comp.name.lower().replace("component", "_component")

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
        elif comp.name == "AutoComponent":
            return ComponentBuilder.generate_auto_component(text, comp)
        elif comp.name == "ButtonComponent":
            return ComponentBuilder.generate_button_component(text, comp)
        elif comp.name.startswith("ScriptComponent"):
            return ComponentBuilder.generate_script_component(text, comp)
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
            template += f"    {gameobject.name}.add_child({i.name})\n"
        template = template.replace("{CHILDS}\n", "")

        return text.replace("{ENTITIES}", template)

    @staticmethod
    def generate_scene(text, scene):
        logger.info("GENERATE SCENE : "+scene.name)
        replaces = {
            "{NAME}": str(scene.name),
            "{COLOR}": str(scene.components[0].color),
            "{TIMESCALE}": str(scene.components[1].timescale),
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
        finish = []
        for i in template.replace("{SCENES}\n", "").split("\n"):
            if i.startswith("def launch") or i.startswith("if __name__"):
                finish.append("\n\n"+i)
            elif "GameObject" in i:
                finish.append("\n"+i)
            elif i != "":
                finish.append(i)

        with open(path, "w") as f:
            f.write("\n".join(finish)+"\n")

    @staticmethod
    def build(project):
        logger.info("BUILD : STARTED")
        ProjectBuilder.project_folders = {
            "main": os.path.join("builds", project.name),
            "files": os.path.join("builds", project.name, "files"),
            "components": os.path.join("builds", project.name, "files", "components"),
            "scripts": os.path.join("builds", project.name, "files", "scripts"),
            "utils": os.path.join("builds", project.name, "files", "utils"),
            "resources": os.path.join("builds", project.name, "resources"),
            "textures": os.path.join("builds", project.name, "resources", "textures"),
            "sounds": os.path.join("builds", project.name, "resources", "sounds")
        }
        ProjectBuilder.components = {"Component": "component"}
        shutil.rmtree(os.path.join("builds", project.name), ignore_errors=True)
        for i in ProjectBuilder.project_folders.values():
            logger.info("CREATE DIR : " + i)
            os.makedirs(i, exist_ok=True)

        logger.info("COPY GAME RESOURCES : STARTED")
        for i in project.textures:
            logger.info("GAME RESOURCE : " + i.components[0].path)
            ext = i.components[0].path.split(".")[-1]
            ComponentBuilder.sprites[i.name] = ext
            shutil.copyfile(
                i.components[0].path,
                os.path.join(ProjectBuilder.project_folders["resources"], i.name+"."+ext)
            )

        for i in project.sounds:
            logger.info("GAME SOUND RESOURCE : " + i.components[0].path)
            ext = i.components[0].path.split(".")[-1]
            ComponentBuilder.sounds[i.name] = ext
            shutil.copyfile(
                i.components[0].path,
                os.path.join(ProjectBuilder.project_folders["sounds"], i.name+"."+ext)
            )
        logger.info("COPY GAME RESOURCES : SUCCESSFULLY ENDED")

        logger.info("COPY GAME SCRIPTS : STARTED")
        with open(os.path.join(ProjectBuilder.project_folders["scripts"], "__init__.py"), "w") as f:
            f.write("from files.scripts.script import Script\n")

        for i in os.listdir(project.folders["scripts"]):
            logger.info("GAME SCRIPT : "+i)
            shutil.copyfile(
                os.path.join(project.folders["scripts"], i),
                os.path.join(ProjectBuilder.project_folders["scripts"], i)
            )
            with open(os.path.join(ProjectBuilder.project_folders["scripts"], "__init__.py"), "a") as f:
                f.write("from files.scripts." + i.replace(".py", "") + " import " + i.replace(".py", "").title() + "\n")

        logger.info("COPY GAME SCRIPT : SUCCESSFULLY ENDED")

        logger.info("GENERATE GAME FILES : STARTED")
        logger.info("GENERATE : Main")
        ProjectBuilder.generate_main(
            os.path.join(ProjectBuilder.project_folders["main"], project.name.title()+".py"),
            project
        )
        logger.info("GENERATE GAME FILES : SUCCESSFULLY ENDED")

        logger.info("COPY CORE FILES : STARTED")
        for i in os.listdir(ProjectBuilder.build_folders["objects"]):
            if i != "components" and i != "scripts" and i != "utils":
                logger.info("CORE FILE : " + i)
                shutil.copyfile(
                    os.path.join(ProjectBuilder.build_folders["objects"], i),
                    os.path.join(ProjectBuilder.project_folders["files"], i)
                )

        with open(os.path.join(ProjectBuilder.project_folders["components"], "__init__.py"), "w") as f:
            f.write("from files.components.component import Component\n")

        for k, v in ProjectBuilder.components.items():
            logger.info("CORE COMPONENT FILE : " + k)
            shutil.copyfile(
                os.path.join(ProjectBuilder.build_folders["components"], v+".py"),
                os.path.join(ProjectBuilder.project_folders["components"], v+".py")
            )
            with open(os.path.join(ProjectBuilder.project_folders["components"], "__init__.py"), "a") as f:
                f.write("from files.components." + v + " import " + k + "\n")

        for i in os.listdir(ProjectBuilder.build_folders["scripts"]):
            logger.info("CORE SCRIPT FILE : " + i)
            shutil.copyfile(
                os.path.join(ProjectBuilder.build_folders["scripts"], i),
                os.path.join(ProjectBuilder.project_folders["scripts"], i)
            )

        shutil.copyfile(
            os.path.join("pyengine", "build", "objects", "utils", "__init__.py"),
            os.path.join(ProjectBuilder.project_folders["utils"], "__init__.py")
        )
        for i in ("color.py", "vec2.py", "math.py"):
            logger.info("CORE UTILS FILE : "+i)
            shutil.copyfile(
                os.path.join(ProjectBuilder.build_folders["utils"], i),
                os.path.join(ProjectBuilder.project_folders["utils"], i)
            )

        logger.info("COPY CORE FILES : SUCCESSFULLY ENDED")

        logger.info("BUILD : SUCCESSFULLY ENDED")
