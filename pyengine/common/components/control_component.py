class ControlComponent:
    def __init__(self):
        self.name = "ControlComponent"
        self.keys = {
            "UPJUMP": "K_UP",
            "LEFT": "K_LEFT",
            "RIGHT": "K_RIGHT",
            "DOWN": "K_DOWN"
        }
        self.control_type = "FOURDIRECTION"
        self.speed = 5

    def to_dict(self):
        return {
            "name": self.name,
            "keys": self.keys,
            "control_type": self.control_type,
            "speed": self.speed
        }

    @classmethod
    def from_dict(cls, values):
        comp = ControlComponent()
        comp.keys = values.get("keys", {"UPJUMP": "K_UP", "LEFT": "K_LEFT", "RIGHT": "K_RIGHT", "DOWN": "K_DOWN"})
        comp.control_type = values.get("control_component", "FOURDIRECTION")
        comp.speed = values.get("speed", 5)
        return comp
