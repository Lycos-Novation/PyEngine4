from pyengine.common.components import *


class GameObject:
    def __init__(self, name):
        self.name = name
        self.childs = []
        self.components = []

    def get_component(self, name):
        for i in self.components:
            if i.name == name:
                return i
        
    def to_dict(self):
        return {
            "name": self.name,
            "childs": [
                i.to_dict() for i in self.childs
            ],
            "components": [
                i.to_dict() for i in self.components
            ]
        }
    
    @classmethod
    def from_dict(cls, values):
        obj = GameObject(values.get("name", "Unknown Object"))
        obj.childs = values.get("childs", [])
        obj.childs = []
        for i in values.get("childs", []):
            obj.childs.append(GameObject.from_dict(i))
        obj.components = []
        for i in values.get("components", []):
            if i.get("name", "") == "ColorComponent":
                obj.components.append(ColorComponent.from_dict(i))
            elif i.get("name", "") == "TransformComponent":
                obj.components.append(TransformComponent.from_dict(i))
            elif i.get("name", "") == "SpriteComponent":
                obj.components.append(SpriteComponent.from_dict(i))
            elif i.get("name", "") == "TextComponent":
                obj.components.append(TextComponent.from_dict(i))
            elif i.get("name", "") == "CollisionComponent":
                obj.components.append(CollisionComponent.from_dict(i))
            elif i.get("name", "") == "BasicPhysicComponent":
                obj.components.append(BasicPhysicComponent.from_dict(i))
            elif i.get("name", "").startswith("ScriptComponent"):
                obj.components.append(ScriptComponent.from_dict(i))
        return obj
