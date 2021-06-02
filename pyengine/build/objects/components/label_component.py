from files.components.component import Component
from files.utils import Vec2

import pygame


class LabelComponent(Component):
    def __init__(self, engine, text, background_color, font_name, font_size, font_bold, font_italic, font_underline,
                 font_color, font_antialias):
        super().__init__(engine)
        self.name = "TextComponent"
        self.text = text
        self.background_color = background_color
        self.font_name = font_name
        self.font_size = font_size
        self.font_bold = font_bold
        self.font_italic = font_italic
        self.font_underline = font_underline
        self.font_color = font_color
        self.font_antialias = font_antialias
        self.transformed_font = None
        self.render = None
        self.update_font()

    def start(self):
        self.update_render()

    def update_font(self):
        try:
            font = pygame.font.Font(self.name, self.font_size)
        except FileNotFoundError:
            font = pygame.font.SysFont(self.name, self.font_size)
        font.set_underline(self.font_underline)
        font.set_italic(self.font_italic)
        font.set_bold(self.font_bold)
        self.transformed_font = font

    def rendered_size(self, text):
        return self.transformed_font.size(text)

    def update_render(self):
        transform = self.game_object.get_component("TransformComponent")
        if transform is not None:
            rotation = transform.global_rotation()
            scale = transform.global_scale()
            render = self.transformed_font.render(self.text, self.font_antialias, self.font_color.rgba())
            render = pygame.transform.rotate(render, rotation)
            self.render = pygame.transform.scale(
                render,
                [int(render.get_rect().width * scale.x), int(render.get_rect().height * scale.y)]
            )

    def show(self, screen, camera_pos):
        transform = self.game_object.get_component("TransformComponent")
        if transform is not None:
            position = transform.global_position()-Vec2(self.render.get_rect().width, self.render.get_rect().height)/2
            if self.background_color is not None:
                screen.fill(self.background_color.rgba(), self.render.get_rect(x=position.x, y=position.y))
            screen.blit(self.render, position.coords())
