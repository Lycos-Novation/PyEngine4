from pyengine.common.components.component import Component
from pyengine.common.utils import Color, Vec2


class ParticleComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "ParticleComponent"
        self.color = Color.from_rgb(255, 255, 255)
        self.final_color = Color.from_rgb(255, 255, 255)
        self.size = Vec2(20, 20)
        self.final_size = Vec2(20, 20)
        self.angle_range = Vec2(0, 359)
        self.force_range = Vec2(50, 50)
        self.offset_min = Vec2(0, 0)
        self.offset_max = Vec2(0, 0)
        self.lifetime = 2
        self.spawn_time = 1
        self.spawn_number = 1

    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color.rgba(),
            "final_color": self.final_color.rgba(),
            "size": self.size.coords(),
            "final_size": self.final_size.coords(),
            "angle_range": self.angle_range.coords(),
            "force_range": self.force_range.coords(),
            "offset_min": self.offset_min.coords(),
            "offset_max": self.offset_max.coords(),
            "lifetime": self.lifetime,
            "spawn_time": self.spawn_time,
            "spawn_number": self.spawn_number
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = ParticleComponent(game_object)
        comp.color = Color.from_rgba(*values.get("color", (255, 255, 255, 255)))
        comp.final_color = Color.from_rgba(*values.get("final_color", (255, 255, 255, 255)))
        comp.size = Vec2(*values.get("size", (20, 20)))
        comp.final_size = Vec2(*values.get("final_size", (20, 20)))
        comp.angle_range = Vec2(*values.get("angle_range", (0, 359)))
        comp.force_range = Vec2(*values.get("force_range", (50, 50)))
        comp.offset_min = Vec2(*values.get("offset_min", (0, 0)))
        comp.offset_max = Vec2(*values.get("offset_max", (0, 0)))
        comp.lifetime = values.get("lifetime", 2)
        comp.spawn_time = values.get("spawn_time", 1)
        comp.spawn_number = values.get("spawn_number", 1)
        return comp
