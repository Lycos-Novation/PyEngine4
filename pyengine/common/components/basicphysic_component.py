class BasicPhysicComponent:
    def __init__(self):
        self.name = "BasicPhysicComponent"
        self.gravity = 125

    def to_dict(self):
        return {
            "name": self.name,
            "gravity": self.gravity
        }

    @classmethod
    def from_dict(cls, values):
        comp = BasicPhysicComponent()
        comp.gravity = values.get("gravity", 125)
        return comp
