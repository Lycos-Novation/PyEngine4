from pyengine.main_window.components.sprite_component import SpriteComponent


class ImageComponent(SpriteComponent):
    def __init__(self, parent, component):
        super().__init__(parent, component)
        self.name.setText("Image")
