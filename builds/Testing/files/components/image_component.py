from files.components.component import Component
from files.utils import Vec2

import pygame
import os


class ImageComponent(Component):
    def __init__(self, engine, sprite):
        super().__init__(engine)

        if sprite == "None":
            sprite = None

        self.name = "ImageComponent"
        self.sprite = sprite
        self.render = None

    def start(self):
        self.update_render()

    def update_render(self):
        if self.sprite is not None:
            transform = self.game_object.get_component("TransformComponent")
            if transform is not None:
                rotation = transform.global_rotation()
                scale = transform.global_scale()
                image = pygame.image.load(os.path.join("resources", "textures", self.sprite)).convert_alpha()
                image = pygame.transform.rotate(image, rotation)
                self.render = pygame.transform.scale(
                    image,
                    [int(image.get_rect().width * scale.x), int(image.get_rect().height * scale.y)]
                )
        else:
            self.render = None

    def show(self, screen, camera_pos):
        if self.render is not None:
            transform = self.game_object.get_component("TransformComponent")
            if transform is not None:
                position = transform.global_position() - Vec2(self.render.get_rect().width,
                                                              self.render.get_rect().height) / 2
                screen.blit(self.render, position.coords())
