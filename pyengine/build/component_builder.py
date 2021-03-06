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
    def generate_particle_component(text, comp):
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{COLOR}": str(comp.color),
            "{FINAL_COLOR}": str(comp.final_color),
            "{SIZE}": str(comp.size),
            "{FINAL_SIZE}": str(comp.final_size),
            "{ANGLE_RANGE}": str(comp.angle_range),
            "{FORCE_RANGE}": str(comp.force_range),
            "{OFFSET_MIN}": str(comp.offset_min),
            "{OFFSET_MAX}": str(comp.offset_max),
            "{LIFETIME}": str(comp.lifetime),
            "{SPAWN_TIME}": str(comp.spawn_time),
            "{SPAWN_NUMBER}": str(comp.spawn_number)
        }

        with open(os.path.join(ComponentBuilder.templates, "particle_component.txt"), "r") as f:
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
            "{CALLBACK}": str(comp.callback),
            "{SIZE}": str(comp.size)
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
    def generate_label_component(text, comp):
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{TEXT}": str(comp.text),
            "{BACKGROUND_COLOR}": "None" if comp.background_transparent else str(comp.background_color),
            "{FONT_NAME}": str(comp.font_name),
            "{FONT_SIZE}": str(comp.font_size),
            "{FONT_BOLD}": str(comp.font_bold),
            "{FONT_ITALIC}": str(comp.font_italic),
            "{FONT_UNDERLINE}": str(comp.font_underline),
            "{FONT_COLOR}": str(comp.font_color),
            "{FONT_ANTIALIAS}": str(comp.font_antialias)
        }

        with open(os.path.join(ComponentBuilder.templates, "label_component.txt"), "r") as f:
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
            "{BACKGROUND_COLOR}": "None" if comp.background_transparent else str(comp.background_color),
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
    def generate_image_component(text, comp):
        if ComponentBuilder.sprites[comp.sprite] is not None:
            sprite = str(comp.sprite)+"."+ComponentBuilder.sprites[comp.sprite]
        else:
            sprite = None
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{SPRITE}": str(sprite)
        }

        with open(os.path.join(ComponentBuilder.templates, "image_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

    @staticmethod
    def generate_sprite_component(text, comp):
        if ComponentBuilder.sprites[comp.sprite] is not None:
            sprite = str(comp.sprite)+"."+ComponentBuilder.sprites[comp.sprite]
        else:
            sprite = None
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{SPRITE}": str(sprite)
        }

        with open(os.path.join(ComponentBuilder.templates, "sprite_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

    @staticmethod
    def generate_music_component(text, comp):
        if ComponentBuilder.sounds[comp.music] is not None:
            music = str(comp.music)+"."+ComponentBuilder.sounds[comp.music]
        else:
            music = None
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{MUSIC}": str(music),
            "{VOLUME}": str(comp.volume),
            "{PLAY}": str(comp.play),
            "{LOOP}": str(comp.loop)
        }

        with open(os.path.join(ComponentBuilder.templates, "music_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

    @staticmethod
    def generate_sound_component(text, comp):
        if ComponentBuilder.sounds[comp.sound] is not None:
            sound = str(comp.sound)+"."+ComponentBuilder.sounds[comp.sound]
        else:
            sound = None
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{SOUND}": str(sound),
            "{VOLUME}": str(comp.volume)
        }

        with open(os.path.join(ComponentBuilder.templates, "sound_component.txt"), "r") as f:
            template = f.read()

        # GENERATE MAIN INFO
        for k, v in replaces.items():
            template = template.replace(k, v)

        return text.replace("{COMPONENTS}", template)

    @staticmethod
    def generate_spritesheet_component(text, comp):
        if ComponentBuilder.sprites[comp.sprite] is not None:
            sprite = str(comp.sprite)+"."+ComponentBuilder.sprites[comp.sprite]
        else:
            sprite = None
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{SPRITE}": str(sprite),
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
    def generate_anim_component(text, comp):
        anims = []
        for i in comp.anims:
            anim = i.to_dict()
            if anim["type"] == "Sprite":
                anim["sprites"] = [str(y)+"."+ComponentBuilder.sprites[y] for y in anim["sprites"]]
            elif anim["type"] == "Sheet":
                anim["sprite_sheet"] = str(anim["sprite_sheet"])+"."+ComponentBuilder.sprites[anim["sprite_sheet"]]
            anims.append(anim)
        replaces = {
            "{NAME}": str(comp.name.lower()),
            "{ANIMS}": str(anims),
            "{FPS}": str(comp.fps),
            "{PLAYING}": str(comp.playing)
        }

        with open(os.path.join(ComponentBuilder.templates, "anim_component.txt"), "r") as f:
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
