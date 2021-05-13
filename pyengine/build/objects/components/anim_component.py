from files.components.component import Component

import pygame
import os


class AnimSprite:
    def __init__(self, name, sprites):
        self.name = name
        self.sprites = sprites
        self.type_ = "Sprite"

    def get_render(self, index, transform):
        if transform is not None:
            rotation = transform.global_rotation()
            scale = transform.global_scale()
            image = pygame.image.load(os.path.join("resources", "textures", self.sprites[index])).convert_alpha()
            image = pygame.transform.rotate(image, rotation)
            return pygame.transform.scale(
                image,
                [int(image.get_rect().width * scale.x), int(image.get_rect().height * scale.y)]
            )

    def __len__(self):
        return len(self.sprites)


class AnimSpriteSheet:
    def __init__(self, name, sprite_sheet, sprite_number):
        self.name = name
        self.sprite_sheet = sprite_sheet
        self.type_ = "Sheet"
        self.sprite_number = sprite_number

    def get_render(self, index, transform):
        if transform is not None:
            rotation = transform.global_rotation()
            scale = transform.global_scale()
            image = pygame.image.load(os.path.join("resources", "textures", self.sprite_sheet)).convert_alpha()
            x_diff = image.get_rect().width // self.sprite_number[0]
            y_diff = image.get_rect().height // self.sprite_number[1]
            indexes = (
                index % self.sprite_number[0],
                index // self.sprite_number[0]
            )
            image = image.subsurface(pygame.Rect(indexes[0]*x_diff, indexes[1]*y_diff, x_diff, y_diff))
            image = pygame.transform.rotate(image, rotation)
            return pygame.transform.scale(
                image,
                [int(image.get_rect().width * scale.x), int(image.get_rect().height * scale.y)]
            )

    def __len__(self):
        return self.sprite_number[0] * self.sprite_number[1]


class AnimComponent(Component):
    def __init__(self, engine, anims, fps, playing):
        super().__init__(engine)

        self.name = "AnimComponent"
        self.__fps = fps
        self.__playing = playing
        self.current_sprite = 0
        self.__timer = 0
        self.anims = {}
        for i in anims:
            if i.get("type", "") == "Sprite":
                self.anims[i.get("name", "Unknown")] = AnimSprite(
                    i.get("name", "Unknown"),
                    i.get("sprites", [])
                )
            elif i.get("type", "") == "Sheet":
                self.anims[i.get("name", "Unknown")] = AnimSpriteSheet(
                    i.get("name", "Unknown"),
                    i.get("sprite_sheet", None),
                    i.get("sprite_number", [1, 1])
                )
        self.render = None

    @property
    def playing(self):
        return self.__playing

    @playing.setter
    def playing(self, value):
        self.__playing = value
        self.current_sprite = 0
        self.__timer = 0

    @property
    def fps(self):
        return self.__fps

    @fps.setter
    def fps(self, value):
        self.__fps = value
        self.current_sprite = 0
        self.__timer = 0

    def update(self, deltatime):
        goal = 1/self.fps
        self.__timer += deltatime
        if self.__timer >= goal:
            self.__timer = 0
            self.current_sprite += 1
            if self.playing == "" or len(self.anims[self.playing]) == self.current_sprite:
                self.current_sprite = 0
            if self.playing in self.anims.keys():
                self.render = self.anims[self.playing].get_render(
                    self.current_sprite,
                    self.game_object.get_component("TransformComponent")
                )
            else:
                self.render = None

    def show(self, screen, camera_pos):
        if self.render is not None:
            transform = self.game_object.get_component("TransformComponent")
            if transform is not None:
                position = transform.global_position() - camera_pos
                screen.blit(self.render, position.coords())
