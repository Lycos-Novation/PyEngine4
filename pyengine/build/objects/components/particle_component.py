from files.components.component import Component


class ParticleComponent(Component):
    def __init__(self, engine, color, final_color, size, final_size, direction, random_direction, lifetime):
        super().__init__(engine)
        self.color = color
        self.final_color = final_color
        self.size = size
        self.final_size = final_size
        self.direction = direction
        self.random_direction = random_direction
        self.lifetime = lifetime
