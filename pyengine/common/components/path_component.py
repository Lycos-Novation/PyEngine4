from pyengine.common.components.component import Component


class PathComponent(Component):
    def __init__(self, game_object, path, type_):
        super().__init__(game_object)
        self.name = "PathComponent"
        self.path = path
        self.type = type_
    
    def to_dict(self):
        return {
            "name": self.name,
            "path": self.path,
            "type": self.type
        }
    
    @classmethod
    def from_dict(cls, game_object, values):
        comp = PathComponent(game_object, values.get("path", ""), values.get("type", ""))
        return comp
