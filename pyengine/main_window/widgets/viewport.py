from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QPainter, QPixmap
from PyQt5.QtCore import QPoint

from pyengine.common.utils import Vec2

import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '5,35'
pygame.init()


class Viewport(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.image = None
        display = (1, 1)
        depth = 32
        flags = 0
        pygame.display.set_mode(display, flags, depth)

    def update_screen(self):
        screen = pygame.Surface(
            (self.parent.project.settings.get("width", 1080), self.parent.project.settings.get("height", 720))
        )
        if self.parent.scene_tree.scene is not None:
            screen.fill(self.parent.scene_tree.scene.get_component("ColorComponent").color.rgba())
            camera_pos = self.parent.scene_tree.scene.get_component("CameraComponent").position
        else:
            screen.fill((0, 0, 0))
            camera_pos = Vec2(0, 0)

        if self.parent.scene_tree.scene is not None:
            objs = [self.parent.scene_tree.scene]
            while len(objs) > 0:
                parent = objs[0]
                del objs[0]
                for child in parent.childs:
                    transform = child.get_component("TransformComponent")
                    if transform is not None:
                        sprite = child.get_component("SpriteComponent")
                        spritesheet = child.get_component("SpriteSheetComponent")
                        text = child.get_component("TextComponent")
                        button = child.get_component("ButtonComponent")
                        anim = child.get_component("AnimComponent")
                        label = child.get_component("LabelComponent")
                        image = child.get_component("ImageComponent")
                        position = transform.global_position()
                        rotation = transform.global_rotation()
                        scale = transform.global_scale()

                        # RENDER BUTTON COMPONENT
                        if button is not None:
                            render = pygame.Surface(button.size.coords(), pygame.SRCALPHA, 32).convert_alpha()
                            render.fill(button.bg.rgba())

                            try:
                                font = pygame.font.Font(button.font_name, button.font_size)
                            except FileNotFoundError:
                                font = pygame.font.SysFont(button.font_name, button.font_size)
                            font.set_underline(button.font_underline)
                            font.set_italic(button.font_italic)
                            font.set_bold(button.font_bold)
                            text_render = font.render(button.text, button.font_antialias, button.font_color.rgba())

                            x = button.size.x - render.get_rect().width / 2 - text_render.get_rect().width / 2
                            y = button.size.y - render.get_rect().height / 2 - text_render.get_rect().height / 2
                            render.blit(text_render, (x, y))
                            render = pygame.transform.rotate(render, rotation)
                            render = pygame.transform.scale(
                                render,
                                [int(render.get_rect().width * scale.x), int(render.get_rect().height * scale.y)]
                            )
                            screen.blit(render,
                                        (position - Vec2(render.get_rect().width,
                                                         render.get_rect().height) / 2).coords())

                        # RENDER SPRITE COMPONENT
                        if sprite is not None and sprite.sprite is not None:
                            path = self.parent.project.get_texture(sprite.sprite).components[0].path
                            if path is not None:
                                render = pygame.image.load(path).convert_alpha()
                                render = pygame.transform.rotate(render, rotation)
                                render = pygame.transform.scale(
                                    render,
                                    [int(render.get_rect().width * scale.x), int(render.get_rect().height * scale.y)]
                                )
                                screen.blit(render,
                                            (position - Vec2(render.get_rect().width,
                                                             render.get_rect().height) / 2 - camera_pos).coords())

                        # RENDER IMAGE COMPONENT
                        if image is not None and image.sprite is not None:
                            path = self.parent.project.get_texture(image.sprite).components[0].path
                            if path is not None:
                                render = pygame.image.load(path).convert_alpha()
                                render = pygame.transform.rotate(render, rotation)
                                render = pygame.transform.scale(
                                    render,
                                    [int(render.get_rect().width * scale.x), int(render.get_rect().height * scale.y)]
                                )
                                screen.blit(render,
                                            (position - Vec2(render.get_rect().width,
                                                             render.get_rect().height) / 2).coords())

                        # RENDER SPRITESHEET COMPONENT
                        if spritesheet is not None and spritesheet.sprite is not None:
                            path = self.parent.project.get_texture(spritesheet.sprite).components[0].path
                            if path is not None:
                                image = pygame.image.load(path).convert_alpha()
                                x_diff = image.get_rect().width // spritesheet.sprite_number[0]
                                y_diff = image.get_rect().height // spritesheet.sprite_number[1]
                                indexes = (
                                    spritesheet.current_sprite % spritesheet.sprite_number[0],
                                    spritesheet.current_sprite // spritesheet.sprite_number[0]
                                )
                                render = image.subsurface(pygame.Rect(indexes[0]*x_diff, indexes[1]*y_diff, x_diff, y_diff))
                                render = pygame.transform.rotate(render, rotation)
                                render = pygame.transform.scale(
                                    render,
                                    [int(render.get_rect().width * scale.x), int(render.get_rect().height * scale.y)]
                                )
                                screen.blit(render,
                                            (position - Vec2(render.get_rect().width,
                                                             render.get_rect().height) / 2 - camera_pos).coords())

                        # RENDER LABEL COMPONENT
                        if label is not None:
                            try:
                                font = pygame.font.Font(label.font_name, label.font_size)
                            except FileNotFoundError:
                                font = pygame.font.SysFont(label.font_name, label.font_size)
                            font.set_underline(label.font_underline)
                            font.set_italic(label.font_italic)
                            font.set_bold(label.font_bold)
                            render = font.render(label.text, label.font_antialias, label.font_color.rgba())
                            render = pygame.transform.rotate(render, rotation)
                            render = pygame.transform.scale(
                                render,
                                [int(render.get_rect().width * scale.x), int(render.get_rect().height * scale.y)]
                            )
                            temp = (position - Vec2(render.get_rect().width, render.get_rect().height) / 2)
                            if not label.background_transparent:
                                screen.fill(label.background_color.rgba(), render.get_rect(x=temp.x, y=temp.y))
                            screen.blit(render, temp.coords())

                        # RENDER TEXT COMPONENT
                        if text is not None:
                            try:
                                font = pygame.font.Font(text.font_name, text.font_size)
                            except FileNotFoundError:
                                font = pygame.font.SysFont(text.font_name, text.font_size)
                            font.set_underline(text.font_underline)
                            font.set_italic(text.font_italic)
                            font.set_bold(text.font_bold)
                            render = font.render(text.text, text.font_antialias, text.font_color.rgba())
                            render = pygame.transform.rotate(render, rotation)
                            render = pygame.transform.scale(
                                render,
                                [int(render.get_rect().width * scale.x), int(render.get_rect().height * scale.y)]
                            )
                            temp = (position - Vec2(render.get_rect().width, render.get_rect().height) / 2 - camera_pos)
                            if not text.background_transparent:
                                screen.fill(text.background_color.rgba(), render.get_rect(x=temp.x, y=temp.y))
                            screen.blit(render, temp.coords())

                        # RENDER ANIM COMPONENT
                        if anim is not None:
                            if anim.playing != "":
                                for i in anim.anims:
                                    if i.name == anim.playing:
                                        if i.type_ == "Sprite":
                                            path = self.parent.project.get_texture(i.sprites[0]).components[0].path
                                            if path is not None:
                                                render = pygame.image.load(path).convert_alpha()
                                                render = pygame.transform.rotate(render, rotation)
                                                render = pygame.transform.scale(
                                                    render,
                                                    [int(render.get_rect().width * scale.x),
                                                     int(render.get_rect().height * scale.y)]
                                                )
                                                screen.blit(render,
                                                            (position -
                                                             Vec2(render.get_rect().width, render.get_rect().height) / 2
                                                             - camera_pos).coords())
                                        elif i.type_ == "Sheet":
                                            path = self.parent.project.get_texture(i.sprite_sheet).components[
                                                0].path
                                            if path is not None:
                                                image = pygame.image.load(path).convert_alpha()
                                                x_diff = image.get_rect().width // i.sprite_number[0]
                                                y_diff = image.get_rect().height // i.sprite_number[1]
                                                render = image.subsurface(
                                                    pygame.Rect(0, 0, x_diff,
                                                                y_diff))
                                                render = pygame.transform.rotate(render, rotation)
                                                render = pygame.transform.scale(
                                                    render,
                                                    [int(render.get_rect().width * scale.x),
                                                     int(render.get_rect().height * scale.y)]
                                                )
                                                screen.blit(render,
                                                            (position -
                                                             Vec2(render.get_rect().width, render.get_rect().height) / 2
                                                             - camera_pos).coords())
                                        break
                    objs.append(child)

        w = screen.get_width()
        h = screen.get_height()

        data = screen.get_buffer().raw
        self.image = QImage(data, w, h, QImage.Format_RGB32)
        self.update()

    def paintEvent(self, evt):
        qp = QPainter(self)
        qp.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform, 1)
        center = QPoint(self.width()/2, self.height()/2)
        qp.translate(center)

        qp.scale(self.width() / self.image.width(), self.height() / self.image.height())

        qp.translate(-self.image.width()/2, -self.image.height()/2)
        qp.drawPixmap(0, 0, self.image.width(), self.image.height(), QPixmap.fromImage(self.image))
