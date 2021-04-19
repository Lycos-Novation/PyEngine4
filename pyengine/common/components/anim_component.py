from pyengine.common.components.component import Component


class AnimSprite:
    def __init__(self, name, sprites):
        self.name = name
        self.sprites = sprites
        self.type_ = "Sprite"

    def to_dict(self):
        return {
            "name": self.name,
            "sprites": self.sprites,
            "type": self.type_
        }

    @classmethod
    def from_dict(cls, values):
        anim = AnimSprite(
            values.get("name", "Unknown"),
            values.get("sprites", [])
        )
        return anim


class AnimSpriteSheet:
    def __init__(self, name, sprite_sheet):
        self.name = name
        self.sprite_sheet = sprite_sheet
        self.type_ = "Sheet"
        self.sprite_number = [1, 1]

    def to_dict(self):
        return {
            "name": self.name,
            "sprite_sheet": self.sprite_sheet,
            "type": self.type_,
            "sprite_number": self.sprite_number
        }

    @classmethod
    def from_dict(cls, values):
        anim = AnimSpriteSheet(
            values.get("name", "Unknown"),
            values.get("sprite_sheet", None)
        )
        anim.sprite_number = values.get("sprite_number", [1, 1])
        return anim


class AnimComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "AnimComponent"
        self.anims = []
        self.fps = 10
        self.playing = ""

    def to_dict(self):
        return {
            "name": self.name,
            "anims": [i.to_dict() for i in self.anims],
            "fps": self.fps,
            "playing": self.playing
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = AnimComponent(game_object)
        comp.anims = []
        for i in values.get("anims", []):
            if i.get("type", "") == "Sprite":
                comp.anims.append(AnimSprite.from_dict(i))
            elif i.get("type", "") == "Sheet":
                comp.anims.append(AnimSpriteSheet.from_dict(i))
        comp.fps = values.get("fps", 10)
        comp.playing = values.get("playing", "")
        return comp
