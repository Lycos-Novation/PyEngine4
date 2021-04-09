import json
import os

from pyengine.common.project_objects.gameobject import GameObject
from pyengine.common.components import PathComponent


class Texture(GameObject):
    def __init__(self, name, path):
        super().__init__(name)
        self.components.append(PathComponent(self, path, "Image (*.png *.jpg)"))
    
    def save(self, directory):
        values = {
            "name": self.name,
            "path": self.components[0].path
        }
        with open(os.path.join(directory, self.name+".json"), "w") as f:
            f.write(json.dumps(values, indent=4))
    
    @classmethod
    def load(cls, file):
        with open(file, "r") as f:
            values = json.load(f)
        texture = Texture(values.get("name", "Unknown Texture"), values.get("path", ""))
        if texture.components[0].path is None or os.path.exists(texture.components[0].path):
            return texture, None
        else:
            path, texture.components[0].path = texture.components[0].path, None
            return texture, "Unknown path : "+path+"\nThis path will be set to None."
