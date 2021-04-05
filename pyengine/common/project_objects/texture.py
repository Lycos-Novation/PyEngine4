import json
import os

from pyengine.common.project_objects.gameobject import GameObject
from pyengine.common.components import PathComponent


class Texture(GameObject):
    def __init__(self, name, path):
        super().__init__(name)
        self.components.append(PathComponent(self, path))
    
    def save(self, directory):
        values = {
            "name": self.name,
            "path": self.components[0].path
        }
        with open(os.path.join(directory, self.name+".json"), "w") as f:
            f.write(json.dumps(values, indent=4))
    
    @classmethod
    def load(cls, file):
        print(file)
        with open(file, "r") as f:
            values = json.load(f)
        texture = Texture(values.get("name", "Unknown Texture"), values.get("path", ""))
        return texture
