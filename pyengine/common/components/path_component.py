from pyengine.common.components.component import Component


class PathComponent(Component):
    def __init__(self, game_object, path):
        super().__init__(game_object)
        self.name = "PathComponent"
        self.path = path
    
    def to_dict(self):
        return {
            "name": self.name,
            "path": self.path
        }
    
    @classmethod
    def from_dict(cls, game_object, values):
        comp = PathComponent(game_object, values.get("path", ""))
        return comp
