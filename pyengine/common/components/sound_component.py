from pyengine.common.components.component import Component


class SoundComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "SoundComponent"
        self.volume = 100
        self.sound = None

    def to_dict(self):
        return {
            "name": self.name,
            "volume": self.volume,
            "sound": self.sound
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = cls(game_object)
        comp.volume = values.get("volume", 100)
        comp.sound = values.get("sound", None)
        return comp
