from pyengine.common.components.component import Component


class CollisionComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "CollisionComponent"
        self.solid = True
        self.callback = None

    def to_dict(self):
        return {
            "name": self.name,
            "solid": self.solid,
            "callback": self.callback
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = CollisionComponent(game_object)
        comp.solid = values.get("solid", True)
        comp.callback = values.get("callback", None)
        return comp
