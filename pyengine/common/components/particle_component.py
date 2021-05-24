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
        self.direction = Vec2(0, 0)
        self.random_direction = False
        self.lifetime = 2

    def to_dict(self):
        return {
            "name": self.name,
            "color": self.color.rgba(),
            "final_color": self.final_color.rgba(),
            "size": self.size.coords(),
            "final_size": self.final_size.coords(),
            "direction": self.direction.coords(),
            "random_direction": self.random_direction,
            "lifetime": self.lifetime
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = ParticleComponent(game_object)
        comp.color = Color.from_rgba(*values.get("color", (255, 255, 255, 255)))
        comp.final_color = Color.from_rgba(*values.get("final_color", (255, 255, 255, 255)))
        comp.size = Vec2(*values.get("size", (20, 20)))
        comp.final_size = Vec2(*values.get("final_size", (20, 20)))
        comp.direction = Vec2(*values.get("direction", (0, 0)))
        comp.random_direction = values.get("random_direction", False)
        comp.lifetime = values.get("lifetime", 2)
        return comp
