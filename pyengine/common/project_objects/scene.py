import json
import os

from pyengine.common.project_objects.gameobject import GameObject
from pyengine.common.components import ColorComponent, TimeScaleComponent, CameraComponent


class Scene(GameObject):
    def __init__(self, name):
        super().__init__(name)
        self.components.append(ColorComponent(self))
        self.components.append(TimeScaleComponent(self))
        self.components.append(CameraComponent(self))
    
    def save(self, directory):
        values = {
            "name": self.name,
            "childs": [
                i.to_dict() for i in self.childs
            ],
            "components": [
                i.to_dict() for i in self.components
            ]
        }
        with open(os.path.join(directory, self.name+".json"), "w") as f:
            f.write(json.dumps(values, indent=4))
    
    @classmethod
    def load(cls, file):
        with open(file, "r") as f:
            values = json.load(f)
        scene = Scene(values.get("name", "Unknown Scene"))

        scene.childs = []
        for i in values.get("childs", []):
            scene.childs.append(GameObject.from_dict(i))

        scene.components = []
        for i in values.get("components", []):
            if i.get("name", "") == "ColorComponent":
                scene.components.append(ColorComponent.from_dict(scene, i))
            elif i.get("name", "") == "TimeScaleComponent":
                scene.components.append(TimeScaleComponent.from_dict(scene, i))
            elif i.get("name", "") == "CameraComponent":
                scene.components.append(CameraComponent.from_dict(scene, i))

        names = [i.name for i in scene.components]
        if "ColorComponent" not in names:
            scene.components.append(ColorComponent(scene))
        if "TimeScaleComponent" not in names:
            scene.components.append(TimeScaleComponent(scene))
        if "CameraComponent" not in names:
            scene.components.append(CameraComponent(scene))

        return scene
