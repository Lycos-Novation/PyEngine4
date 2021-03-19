import os


class ComponentBuilder:
    templates = os.path.join("pyengine", "build", "templates", "components")
    sprites = {}

    @staticmethod
    def generate_sprite_component(text, comp):
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{SPRITE}": str(comp.sprite)+"."+ComponentBuilder.sprites[comp.sprite]
        }
        with open(os.path.join(ComponentBuilder.templates, "sprite_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

    @staticmethod
    def generate_transform_component(text, comp):
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{POSITION}": str(comp.position),
            "{ROTATION}": str(comp.rotation),
            "{SCALE}": str(comp.scale)
        }
        with open(os.path.join(ComponentBuilder.templates, "transform_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)
