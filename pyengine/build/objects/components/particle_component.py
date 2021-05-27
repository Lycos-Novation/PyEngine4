from files.components.component import Component
from files.utils import Vec2

from random import randint
import math


class Particle:
    def __init__(self, system, start_pos, lifetime, direction, size, final_size, color, final_color):
        self.system = system
        self.color = color
        self.final_color = final_color
        self.current_color = color
        self.size = size
        self.final_size = final_size
        self.current_size = size
        self.direction = direction
        self.position = start_pos
        self.lifetime = lifetime
        self.time = 0

    def update(self, deltatime):
        self.time += deltatime
        if self.time > self.lifetime:
            self.system.remove_particle(self)
        else:
            self.position += self.direction * deltatime

        if self.color != self.final_color:
            p = self.time / self.lifetime
            self.current_color = self.color * (1 - p) + self.final_color * p

        if self.size != self.final_size:
            p = self.time / self.lifetime
            self.current_size = self.size * (1 - p) + self.final_size * p

    def show(self, screen, camera_pos):
        screen.fill(self.current_color.rgba(), ((self.position - camera_pos).coords(),
                                                self.current_size.coords()))


class ParticleComponent(Component):
    def __init__(self, engine, color, final_color, size, final_size, angle_range, force_range, lifetime, spawn_time,
                 spawn_number):
        super().__init__(engine)
        self.name = "ParticleComponent"
        self.color = color
        self.final_color = final_color
        self.size = size
        self.final_size = final_size
        self.angle_range = angle_range
        self.force_range = force_range
        self.lifetime = lifetime
        self.spawn_time = spawn_time
        self.spawn_number = spawn_number
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
                for i in range(self.spawn_number):
                    force = randint(self.force_range.x, self.force_range.y)
                    angle = math.radians(randint(self.angle_range.x, self.angle_range.y))
                    self.particles.append(Particle(self, position, self.lifetime,
                                                   Vec2(force*math.cos(angle), force*math.sin(angle)), self.size,
                                                   self.final_size, self.color, self.final_color))
            for i in self.particles:
                i.update(deltatime)

    def show(self, screen, camera_pos):
        if len(self.particles):
            for i in self.particles:
                i.show(screen, camera_pos)
