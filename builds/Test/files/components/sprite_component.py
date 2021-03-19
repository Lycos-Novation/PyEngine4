from files.components.component import Component

import pygame
import os


class SpriteComponent(Component):
    def __init__(self, sprite):
        super().__init__()
        self.name = "SpriteComponent"
        self.sprite = sprite

    def show(self, screen):
        transform = self.entity.get_component("TransformComponent")
        if transform is not None:
            position = transform.position
            rotation = transform.rotation
            scale = transform.scale
            image = pygame.image.load(os.path.join("resources", self.sprite)).convert_alpha()
            image = pygame.transform.rotate(image, rotation)
            image = pygame.transform.scale(
                image,
                [int(image.get_rect().width * scale[0]), int(image.get_rect().height * scale[1])]
            )
            screen.blit(image, position)
