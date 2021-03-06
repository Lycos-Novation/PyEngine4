from files.components.component import Component
from files.utils import Vec2

import pygame
import os


class SpriteSheetComponent(Component):
    def __init__(self, engine, sprite, sprite_number, current_sprite):
        super().__init__(engine)

        if sprite == "None":
            sprite = None

        self.name = "SpriteSheetComponent"
        self.sprite = sprite
        self.sprite_number = sprite_number
        self.current_sprite = current_sprite
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
                x_diff = image.get_rect().width // self.sprite_number[0]
                y_diff = image.get_rect().height // self.sprite_number[1]
                indexes = (
                    self.current_sprite % self.sprite_number[0],
                    self.current_sprite // self.sprite_number[0]
                )
                image = image.subsurface(pygame.Rect(indexes[0]*x_diff, indexes[1]*y_diff, x_diff, y_diff))
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
                position = transform.global_position() - camera_pos - Vec2(self.render.get_rect().width,
                                                                           self.render.get_rect().height) / 2
                screen.blit(self.render, position.coords())
