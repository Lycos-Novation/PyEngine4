from files.components.component import Component

import pygame


class TextComponent(Component):
    def __init__(self, engine, text, font_name, font_size, font_bold, font_italic, font_underline, font_color,
                 font_antialias):
        super().__init__(engine)
        self.name = "TextComponent"
        self.text = text
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
            render = self.transformed_font.render(self.text, self.font_antialias, self.font_color)
            render = pygame.transform.rotate(render, rotation)
            self.render = pygame.transform.scale(
                render,
                [int(render.get_rect().width * scale[0]), int(render.get_rect().height * scale[1])]
            )

    def show(self, screen):
        transform = self.game_object.get_component("TransformComponent")
        if transform is not None:
            position = transform.global_position()
            screen.blit(self.render, position)
