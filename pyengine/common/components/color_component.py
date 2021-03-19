class ColorComponent:
    def __init__(self):
        self.name = "ColorComponent"
        self.color = [0, 0, 0, 0]
    
    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color
        }
    
    @classmethod
    def from_dict(cls, values):
        color = ColorComponent()
        color.color = values.get("color", [0, 0, 0, 0])
        return color
