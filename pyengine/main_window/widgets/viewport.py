from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QPainter

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
            screen.fill(self.parent.scene_tree.scene.get_component("ColorComponent").color)
        else:
            screen.fill((0, 0, 0))

        if self.parent.scene_tree.scene is not None:
            objs = [self.parent.scene_tree.scene]
            while len(objs) > 0:
                parent = objs[0]
                del objs[0]
                for child in parent.childs:
                    transform = child.get_component("TransformComponent")
                    sprite = child.get_component("SpriteComponent")
                    if transform is not None:
                        if sprite is not None and sprite.sprite is not None:
                            path = self.parent.project.get_texture(sprite.sprite).components[0].path
                            position = transform.position
                            rotation = transform.rotation
                            scale = transform.scale
                            image = pygame.image.load(path).convert_alpha()
                            image = pygame.transform.rotate(image, rotation)
                            image = pygame.transform.scale(
                                image,
                                [int(image.get_rect().width * scale[0]), int(image.get_rect().height * scale[1])]
                            )
                            screen.blit(image, position)
                    objs.append(child)

        w = screen.get_width()
        h = screen.get_height()

        data = screen.get_buffer().raw
        self.image = QImage(data, w, h, QImage.Format_RGB32)
        self.update()

    def paintEvent(self, evt):
        qp = QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.image)
        qp.end()
