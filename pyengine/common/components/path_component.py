class PathComponent:
    def __init__(self, path):
        self.name = "PathComponent"
        self.path = path
    
    def to_dict(self):
        return {
            "name": self.name,
            "path": self.path
        }
    
    @classmethod
    def from_dict(cls, values):
        comp = PathComponent(values.get("path", ""))
        return comp
