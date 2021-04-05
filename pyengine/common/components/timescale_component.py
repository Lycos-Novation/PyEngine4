from pyengine.common.components.component import Component


class TimeScaleComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "TimeScaleComponent"
        self.timescale = 1

    def to_dict(self):
        return {
            "name": self.name,
            "timescale": self.timescale
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = TimeScaleComponent(game_object)
        comp.timescale = values.get("timescale", 1)
        return comp
