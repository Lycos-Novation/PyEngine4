class AutoComponent:
    def __init__(self):
        self.name = "AutoComponent"
        self.move = [0, 0]
        self.rotation = 0
        self.active = True

    def to_dict(self):
        return {
            "name": self.name,
            "move": self.move,
            "rotation": self.rotation,
            "active": self.active
        }

    @classmethod
    def from_dict(cls, values):
        comp = AutoComponent()
        comp.move = values.get("move", [0, 0])
        comp.rotation = values.get("rotation", 0)
        comp.active = values.get("active", True)
        return comp
