import json
import os

from pyengine.common.project_objects.gameobject import GameObject
from pyengine.common.components import PathComponent


class Sound(GameObject):
    def __init__(self, name, path):
        super().__init__(name)
        self.components.append(PathComponent(self, path, "Sound (*.ogg *.wav *.mp3)"))

    def save(self, directory):
        values = {
            "name": self.name,
            "path": self.components[0].path
        }
        with open(os.path.join(directory, self.name + ".json"), "w") as f:
            f.write(json.dumps(values, indent=4))

    @classmethod
    def load(cls, file):
        with open(file, "r") as f:
            values = json.load(f)
        texture = Sound(values.get("name", "Unknown Sound"), values.get("path", ""))
        return texture
