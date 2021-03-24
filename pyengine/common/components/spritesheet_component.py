class SpriteSheetComponent:
    def __init__(self):
        self.name = "SpriteSheetComponent"
        self.sprite = None
        self.sprite_number = [1, 1]
        self.current_sprite = 0

    def to_dict(self):
        return {
            "name": self.name,
            "sprite": self.sprite,
            "sprite_number": self.sprite_number,
            "current_sprite": 0
        }

    @classmethod
    def from_dict(cls, values):
        comp = SpriteSheetComponent()
        comp.sprite = values.get("sprite", None)
        comp.sprite_number = values.get("sprite_number", [1, 1])
        comp.current_sprite = values.get("current_sprite", 0)
        return comp
