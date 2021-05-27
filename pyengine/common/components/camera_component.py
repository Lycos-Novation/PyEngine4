from pyengine.common.components.component import Component
from pyengine.common.utils import Vec2


class CameraComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "CameraComponent"
        self.position = Vec2(0, 0)
        self.follow_entity = None

    def to_dict(self):
        return {
            "name": self.name,
            "position": self.position.coords(),
            "follow_entity": self.follow_entity
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = CameraComponent(game_object)
        comp.position = Vec2(*values.get("position", (0, 0)))
        comp.follow_entity = values.get("follow_entity", None)
        return comp
