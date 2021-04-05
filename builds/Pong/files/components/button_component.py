from files.components.component import Component
import pygame
import pygame.locals


class ButtonComponent(Component):
    def __init__(self, engine, bg, size, callback, text, font_name, font_size, font_bold, font_italic, font_underline,
                 font_color, font_antialias):
        super().__init__(engine)
        self.name = "ButtonComponent"
        self.bg = bg
        self.size = size
        self.callback = callback
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

    def update_render(self):
        transform = self.game_object.get_component("TransformComponent")
        if transform is not None:
            rotation = transform.global_rotation()
            scale = transform.global_scale()
            render = pygame.Surface(self.size.coords(), pygame.SRCALPHA, 32).convert_alpha()
            render.fill(self.bg.rgba())
            text_render = self.transformed_font.render(self.text, self.font_antialias, self.font_color.rgba())
            x = self.size.x - render.get_rect().width / 2 - text_render.get_rect().width / 2
            y = self.size.y - render.get_rect().height / 2 - text_render.get_rect().height / 2
            render.blit(text_render, (x, y))

            render = pygame.transform.rotate(render, rotation)
            self.render = pygame.transform.scale(
                render,
                [int(render.get_rect().width * scale.x), int(render.get_rect().height * scale.y)]
            )

    def show(self, screen):
        transform = self.game_object.get_component("TransformComponent")
        if transform is not None:
            position = transform.global_position()
            screen.blit(self.render, position.coords())

    def mouse_press(self, evt):
        transform = self.game_object.get_component("TransformComponent")
        if transform is not None:
            position = transform.global_position()
            if evt.button == pygame.locals.BUTTON_LEFT and \
                    self.render.get_rect(x=position.x, y=position.y).collidepoint(*evt.pos):
                if self.callback is not None:
                    names = self.callback.split(" - ")
                    eval('self.game_object.get_component("' + names[0] + '").' + names[1] + "()")
