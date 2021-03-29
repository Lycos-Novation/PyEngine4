from pyengine.common.components.component import Component


class ControlComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "ControlComponent"
        self.keys = {
            "UPJUMP": "K_UP",
            "LEFT": "K_LEFT",
            "RIGHT": "K_RIGHT",
            "DOWN": "K_DOWN"
        }
        self.control_type = "FOURDIRECTION"
        self.speed = 200

    def to_dict(self):
        return {
            "name": self.name,
            "keys": self.keys,
            "control_type": self.control_type,
            "speed": self.speed
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = ControlComponent(game_object)
        comp.keys = values.get("keys", {"UPJUMP": "K_UP", "LEFT": "K_LEFT", "RIGHT": "K_RIGHT", "DOWN": "K_DOWN"})
        comp.control_type = values.get("control_type", "FOURDIRECTION")
        comp.speed = values.get("speed", 200)
        return comp
