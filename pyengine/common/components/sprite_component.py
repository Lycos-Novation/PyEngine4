class SpriteComponent:
    def __init__(self):
        self.name = "SpriteComponent"
        self.sprite = None
    
    def to_dict(self):
        return {
            "name": self.name,
            "sprite": self.sprite
        }
    
    @classmethod
    def from_dict(cls, values):
        comp = SpriteComponent()
        comp.sprite = values.get("sprite", None)
        return comp
