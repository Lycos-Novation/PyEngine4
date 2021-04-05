from pyengine.common.components.component import Component
from pyengine.common.utils import Color


class ColorComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "ColorComponent"
        self.color = Color.from_rgb(0, 0, 0)
    
    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color.rgba()
        }
    
    @classmethod
    def from_dict(cls, game_object, values):
        color = ColorComponent(game_object)
        color.color = Color.from_rgba(*values.get("color", (0, 0, 0, 0)))
        return color
