import json
import os

from pyengine.common.project_objects.gameobject import GameObject
from pyengine.common.components import PathComponent


class Lang(GameObject):
    def __init__(self, name, path):
        super().__init__(name)
        self.components.append(PathComponent(self, path, "Lang (*.json)"))

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
        lang = Lang(values.get("name", "Unknown Lang"), values.get("path", ""))
        if lang.components[0].path is None or os.path.exists(lang.components[0].path):
            return lang, None
        else:
            path, lang.components[0].path = lang.components[0].path, None
            return lang, "Unknown path : "+path+"\nThis path will be set to None."
