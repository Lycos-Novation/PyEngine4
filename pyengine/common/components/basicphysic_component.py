from pyengine.common.components.component import Component


class BasicPhysicComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "BasicPhysicComponent"
        self.gravity = 125

    def to_dict(self):
        return {
            "name": self.name,
            "gravity": self.gravity
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = BasicPhysicComponent(game_object)
        comp.gravity = values.get("gravity", 125)
        return comp
