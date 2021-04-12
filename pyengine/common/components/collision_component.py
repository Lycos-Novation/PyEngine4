from pyengine.common.components.component import Component
from pyengine.common.utils import Vec2


class CollisionComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "CollisionComponent"
        self.solid = True
        self.callback = None
        self.size = Vec2.zero()

    def to_dict(self):
        return {
            "name": self.name,
            "solid": self.solid,
            "callback": self.callback,
            "size": self.size.coords()
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = CollisionComponent(game_object)
        comp.solid = values.get("solid", True)
        comp.callback = values.get("callback", None)
        comp.size = Vec2(*values.get("size", (0, 0)))
        return comp
