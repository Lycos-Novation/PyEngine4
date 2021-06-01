from pyengine.common.components.text_component import TextComponent


class LabelComponent(TextComponent):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "LabelComponent"
