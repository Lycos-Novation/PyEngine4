from pyengine.common.components.component import Component


class SpriteComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "SpriteComponent"
        self.sprite = None
    
    def to_dict(self):
        return {
            "name": self.name,
            "sprite": self.sprite
        }
    
    @classmethod
    def from_dict(cls, game_object, values):
        comp = SpriteComponent(game_object)
        comp.sprite = values.get("sprite", None)
        return comp
