class CollisionComponent:
    def __init__(self):
        self.name = "CollisionComponent"
        self.solid = True
        self.callback = None

    def to_dict(self):
        return {
            "name": self.name,
            "solid": self.solid,
            "callback": self.callback
        }

    @classmethod
    def from_dict(cls, values):
        comp = CollisionComponent()
        comp.solid = values.get("solid", True)
        comp.callback = values.get("callback", None)
        return comp
