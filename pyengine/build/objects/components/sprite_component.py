from files.components.component import Component

import pygame
import os


class SpriteComponent(Component):
    def __init__(self, engine, sprite):
        super().__init__(engine)

        if sprite == "None":
            sprite = None

        self.name = "SpriteComponent"
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

    def show(self, screen):
        if self.render is not None:
            transform = self.game_object.get_component("TransformComponent")
            if transform is not None:
                position = transform.global_position()
                screen.blit(self.render, position.coords())
