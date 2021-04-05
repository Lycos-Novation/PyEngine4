from pyengine.common.components.component import Component
from pyengine.common.utils import Vec2


class TransformComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "TransformComponent"
        self.position = Vec2(0, 0)
        self.rotation = 0
        self.scale = Vec2(1, 1)

    def global_position(self):
        position = self.position
        if self.game_object.parent is not None:
            if self.game_object.parent.get_component("TransformComponent") is not None:
                pposition = self.game_object.parent.get_component("TransformComponent").global_position()
                position.x += pposition.x
                position.y += pposition.y
        return position

    def global_rotation(self):
        rotation = self.rotation
        if self.game_object.parent is not None:
            if self.game_object.parent.get_component("TransformComponent") is not None:
                rotation += self.game_object.parent.get_component("TransformComponent").rotation
        return rotation

    def global_scale(self):
        scale = self.scale
        if self.game_object.parent is not None:
            if self.game_object.parent.get_component("TransformComponent") is not None:
                pscale = self.game_object.parent.get_component("TransformComponent").global_scale()
                scale.x += pscale.x
                scale.y += pscale.y
        return scale
    
    def to_dict(self):
        return {
            "name": self.name,
            "position": self.position.coords(),
            "rotation": self.rotation,
            "scale": self.scale.coords()
        }
    
    @classmethod
    def from_dict(cls, game_object, values):
        comp = TransformComponent(game_object)
        comp.position = Vec2(*values.get("position", (0, 0)))
        comp.rotation = values.get("rotation", 0)
        comp.scale = Vec2(*values.get("scale", (1, 1)))
        return comp
