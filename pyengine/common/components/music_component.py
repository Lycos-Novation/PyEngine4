from pyengine.common.components.component import Component


class MusicComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "MusicComponent"
        self.volume = 100
        self.music = None
        self.play = True

    def to_dict(self):
        return {
            "name": self.name,
            "volume": self.volume,
            "music": self.music,
            "play": self.play
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = cls(game_object)
        comp.volume = values.get("volume", 100)
        comp.music = values.get("music", None)
        comp.play = values.get("play", True)
        return comp
