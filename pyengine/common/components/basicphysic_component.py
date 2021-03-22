class BasicPhysicComponent:
    def __init__(self):
        self.name = "BasicPhysicComponent"
        self.gravity = 5

    def to_dict(self):
        return {
            "name": self.name,
            "gravity": self.gravity
        }

    @classmethod
    def from_dict(cls, values):
        comp = BasicPhysicComponent()
        comp.gravity = values.get("gravity", 5)
        return comp
