from pyengine.common.components.component import Component
from pyengine.common.utils import Vec2


class AutoComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "AutoComponent"
        self.move = Vec2(0, 0)
        self.rotation = 0
        self.active = True

    def to_dict(self):
        return {
            "name": self.name,
            "move": self.move.coords(),
            "rotation": self.rotation,
            "active": self.active
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = AutoComponent(game_object)
        comp.move = Vec2(*values.get("move", (0, 0)))
        comp.rotation = values.get("rotation", 0)
        comp.active = values.get("active", True)
        return comp
