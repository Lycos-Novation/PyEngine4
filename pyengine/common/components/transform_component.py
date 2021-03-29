from pyengine.common.components.component import Component


class TransformComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "TransformComponent"
        self.position = [0, 0]
        self.rotation = 0
        self.scale = [1, 1]

    def global_position(self):
        position = self.position.copy()
        if self.game_object.parent is not None:
            if self.game_object.parent.get_component("TransformComponent") is not None:
                pposition = self.game_object.parent.get_component("TransformComponent").global_position()
                position[0] += pposition[0]
                position[1] += pposition[1]
        return position

    def global_rotation(self):
        rotation = self.rotation
        if self.game_object.parent is not None:
            if self.game_object.parent.get_component("TransformComponent") is not None:
                rotation += self.game_object.parent.get_component("TransformComponent").rotation
        return rotation

    def global_scale(self):
        scale = self.scale.copy()
        if self.game_object.parent is not None:
            if self.game_object.parent.get_component("TransformComponent") is not None:
                pscale = self.game_object.parent.get_component("TransformComponent").global_scale()
                scale[0] += pscale[0]
                scale[1] += pscale[1]
        return scale
    
    def to_dict(self):
        return {
            "name": self.name,
            "position": self.position,
            "rotation": self.rotation,
            "scale": self.scale
        }
    
    @classmethod
    def from_dict(cls, game_object, values):
        comp = TransformComponent(game_object)
        comp.position = values.get("position", [0, 0])
        comp.rotation = values.get("rotation", 0)
        comp.scale = values.get("scale", [1, 1])
        return comp
