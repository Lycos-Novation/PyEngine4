from pyengine.common.components.component import Component


class ScriptComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "ScriptComponent "

    def to_dict(self):
        return {
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = cls(game_object)
        comp.name = values.get("name", "")
        return comp
