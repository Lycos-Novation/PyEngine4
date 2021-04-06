import os


class ComponentBuilder:
    templates = os.path.join("pyengine", "build", "templates", "components")
    sprites = {}
    sounds = {}

    @staticmethod
    def generate_script_component(text, comp):
        name = comp.name.split(" ")[-1]
        replaces = {
            "{NAME}": str(name.lower()),
            "{NAMETITLED}": str(name.title())
        }
        with open(os.path.join(ComponentBuilder.templates, "script_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

    @staticmethod
    def generate_control_component(text, comp):
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{KEYS}": str(comp.keys),
            "{CONTROL_TYPE}": str(comp.control_type),
            "{SPEED}": str(comp.speed)
        }

        with open(os.path.join(ComponentBuilder.templates, "control_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

    @staticmethod
    def generate_basicphysic_component(text, comp):
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{GRAVITY}": str(comp.gravity)
        }

        with open(os.path.join(ComponentBuilder.templates, "basicphysic_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

    @staticmethod
    def generate_collision_component(text, comp):
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{SOLID}": str(comp.solid),
            "{CALLBACK}": str(comp.callback)
        }

        with open(os.path.join(ComponentBuilder.templates, "collision_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

    @staticmethod
    def generate_button_component(text, comp):
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{SIZE}": str(comp.size),
            "{BG}": str(comp.bg),
            "{CALLBACK}": str(comp.callback),
            "{TEXT}": str(comp.text),
            "{FONT_NAME}": str(comp.font_name),
            "{FONT_SIZE}": str(comp.font_size),
            "{FONT_BOLD}": str(comp.font_bold),
            "{FONT_ITALIC}": str(comp.font_italic),
            "{FONT_UNDERLINE}": str(comp.font_underline),
            "{FONT_COLOR}": str(comp.font_color),
            "{FONT_ANTIALIAS}": str(comp.font_antialias)
        }

        with open(os.path.join(ComponentBuilder.templates, "button_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

    @staticmethod
    def generate_text_component(text, comp):
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{TEXT}": str(comp.text),
            "{FONT_NAME}": str(comp.font_name),
            "{FONT_SIZE}": str(comp.font_size),
            "{FONT_BOLD}": str(comp.font_bold),
            "{FONT_ITALIC}": str(comp.font_italic),
            "{FONT_UNDERLINE}": str(comp.font_underline),
            "{FONT_COLOR}": str(comp.font_color),
            "{FONT_ANTIALIAS}": str(comp.font_antialias)
        }

        with open(os.path.join(ComponentBuilder.templates, "text_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

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
    def generate_spritesheet_component(text, comp):
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{SPRITE}": str(comp.sprite)+"."+ComponentBuilder.sprites[comp.sprite],
            "{SPRITE_NUMBER}": str(comp.sprite_number),
            "{CURRENT_SPRITE}": str(comp.current_sprite)
        }

        with open(os.path.join(ComponentBuilder.templates, "spritesheet_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

    @staticmethod
    def generate_auto_component(text, comp):
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{MOVE}": str(comp.move),
            "{ROTATION}": str(comp.rotation),
            "{ACTIVE}": str(comp.active)
        }
        with open(os.path.join(ComponentBuilder.templates, "auto_component.txt"), "r") as f:
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
