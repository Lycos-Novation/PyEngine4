class TransformComponent:
    def __init__(self):
        self.name = "TransformComponent"
        self.position = [0, 0]
        self.rotation = 0
        self.scale = [1, 1]
    
    def to_dict(self):
        return {
            "name": self.name,
            "position": self.position,
            "rotation": self.rotation,
            "scale": self.scale
        }
    
    @classmethod
    def from_dict(cls, values):
        comp = TransformComponent()
        comp.position = values.get("position", [0, 0])
        comp.rotation = values.get("rotation", 0)
        comp.scale = values.get("scale", [1, 1])
        return comp
