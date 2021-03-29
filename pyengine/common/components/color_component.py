from pyengine.common.components.component import Component


class ColorComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "ColorComponent"
        self.color = [0, 0, 0, 255]
    
    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color
        }
    
    @classmethod
    def from_dict(cls, game_object, values):
        color = ColorComponent(game_object)
        color.color = values.get("color", [0, 0, 0, 255])
        return color
