from pyengine.common.components import *


class GameObject:
    def __init__(self, name):
        self.name = name
        self.tag = "Object"
        self.zindex = 0
        self.childs = []
        self.components = []
        self.parent = None

    def get_all_childs(self):
        childs = self.childs.copy()
        for i in self.childs:
            childs += i.get_all_childs()
        return childs

    def get_component(self, name):
        for i in self.components:
            if i.name == name:
                return i
        
    def to_dict(self):
        return {
            "name": self.name,
            "tag": self.tag,
            "zindex": self.zindex,
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
        obj.tag = values.get("tag", "Object")
        obj.zindex = values.get("zindex", 0)
        obj.childs = values.get("childs", [])
        obj.childs = []
        for i in values.get("childs", []):
            obj.childs.append(GameObject.from_dict(i))
            obj.childs[-1].parent = obj
        obj.components = []
        for i in values.get("components", []):
            if i.get("name", "") == "ColorComponent":
                obj.components.append(ColorComponent.from_dict(obj, i))
            elif i.get("name", "") == "TransformComponent":
                obj.components.append(TransformComponent.from_dict(obj, i))
            elif i.get("name", "") == "SpriteComponent":
                obj.components.append(SpriteComponent.from_dict(obj, i))
            elif i.get("name", "") == "TextComponent":
                obj.components.append(TextComponent.from_dict(obj, i))
            elif i.get("name", "") == "CollisionComponent":
                obj.components.append(CollisionComponent.from_dict(obj, i))
            elif i.get("name", "") == "BasicPhysicComponent":
                obj.components.append(BasicPhysicComponent.from_dict(obj, i))
            elif i.get("name", "") == "ControlComponent":
                obj.components.append(ControlComponent.from_dict(obj, i))
            elif i.get("name", "") == "SpriteSheetComponent":
                obj.components.append(SpriteSheetComponent.from_dict(obj, i))
            elif i.get("name", "") == "AutoComponent":
                obj.components.append(AutoComponent.from_dict(obj, i))
            elif i.get("name", "") == "MusicComponent":
                obj.components.append(MusicComponent.from_dict(obj, i))
            elif i.get("name", "") == "ButtonComponent":
                obj.components.append(ButtonComponent.from_dict(obj, i))
            elif i.get("name", "") == "SoundComponent":
                obj.components.append(SoundComponent.from_dict(obj, i))
            elif i.get("name", "") == "AnimComponent":
                obj.components.append(AnimComponent.from_dict(obj, i))
            elif i.get("name", "") == "ParticleComponent":
                obj.components.append(ParticleComponent.from_dict(obj, i))
            elif i.get("name", "") == "LabelComponent":
                obj.components.append(LabelComponent.from_dict(obj, i))
            elif i.get("name", "") == "ImageComponent":
                obj.components.append(ImageComponent.from_dict(obj, i))
            elif i.get("name", "").startswith("ScriptComponent"):
                obj.components.append(ScriptComponent.from_dict(obj, i))
        return obj
