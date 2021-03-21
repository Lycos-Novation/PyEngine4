from files.components.component import Component

import pygame
import os


class SpriteComponent(Component):
    def __init__(self, engine, sprite):
        super().__init__(engine)
        self.name = "SpriteComponent"
        self.sprite = sprite
        self.render = None

    def start(self):
        self.update_render()

    def update_render(self):
        transform = self.entity.get_component("TransformComponent")
        if transform is not None:
            rotation = transform.rotation
            scale = transform.scale
            image = pygame.image.load(os.path.join("resources", self.sprite)).convert_alpha()
            image = pygame.transform.rotate(image, rotation)
            self.render = pygame.transform.scale(
                image,
                [int(image.get_rect().width * scale[0]), int(image.get_rect().height * scale[1])]
            )

    def show(self, screen):
        transform = self.entity.get_component("TransformComponent")
        if transform is not None:
            position = transform.position
            screen.blit(self.render, position)
