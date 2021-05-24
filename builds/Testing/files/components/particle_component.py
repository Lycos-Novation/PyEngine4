from files.components.component import Component
from files.utils import Vec2

from random import randint


class Particle:
    def __init__(self, system, start_pos, lifetime, direction, size, final_size, color, final_color):
        self.system = system
        self.color = color
        self.final_color = final_color
        self.size = size
        self.final_size = final_size
        self.direction = direction
        self.position = start_pos
        self.lifetime = lifetime
        self.time = 0
        self.use_position_of_parent = False

    def update(self, deltatime):
        self.time += deltatime
        if self.time > self.lifetime:
            self.system.remove_particle(self)
        else:
            self.position += self.direction * deltatime

    def show(self, screen, component_position, camera_pos):
        if self.use_position_of_parent:
            screen.fill(self.color.rgba(), ((self.position + component_position - camera_pos).coords(),
                                            self.size.coords()))
        else:
            screen.fill(self.color.rgba(), ((self.position - camera_pos).coords(), self.size.coords()))


class ParticleComponent(Component):
    def __init__(self, engine, color, final_color, size, final_size, direction, random_direction, lifetime, spawn_time):
        super().__init__(engine)
        self.color = color
        self.final_color = final_color
        self.size = size
        self.final_size = final_size
        self.direction = direction
        self.random_direction = random_direction
        self.lifetime = lifetime
        self.spawn_time = spawn_time
        self.time = 0
        self.particles = []

    def remove_particle(self, particle):
        self.particles.remove(particle)

    def update(self, deltatime):
        transform = self.game_object.get_component("TransformComponent")
        if transform is not None:
            position = transform.global_position()
            self.time += deltatime
            if self.time > self.spawn_time:
                self.time = 0
                if self.random_direction:
                    self.particles.append(Particle(self, position, self.lifetime,
                                                   Vec2(randint(-50, 50), randint(-50, 50)), self.size, self.final_size,
                                                   self.color, self.final_color))
                else:
                    self.particles.append(Particle(self, position, self.lifetime, self.direction, self.size,
                                                   self.final_size, self.color, self.final_color))
            for i in self.particles:
                i.update(deltatime)

    def show(self, screen, camera_pos):
        if len(self.particles):
            print(len(self.particles))
            transform = self.game_object.get_component("TransformComponent")
            if transform is not None:
                position = transform.global_position()
                for i in self.particles:
                    i.show(screen, position - i.position, camera_pos)
