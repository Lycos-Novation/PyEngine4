from pyengine.common.components.sprite_component import SpriteComponent


class ImageComponent(SpriteComponent):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "ImageComponent"
