from pyengine.common.components.component import Component


class SpriteSheetComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "SpriteSheetComponent"
        self.sprite = None
        self.sprite_number = [1, 1]
        self.current_sprite = 0

    def to_dict(self):
        return {
            "name": self.name,
            "sprite": self.sprite,
            "sprite_number": self.sprite_number,
            "current_sprite": 0
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = SpriteSheetComponent(game_object)
        comp.sprite = values.get("sprite", None)
        comp.sprite_number = values.get("sprite_number", [1, 1])
        comp.current_sprite = values.get("current_sprite", 0)
        return comp
