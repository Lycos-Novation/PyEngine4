from pyengine.common.components.component import Component
from pyengine.common.utils import Color


class TextComponent(Component):
    def __init__(self, game_object):
        super().__init__(game_object)
        self.name = "TextComponent"
        self.text = ""
        self.font_name = "arial"
        self.font_size = 16
        self.font_bold = False
        self.font_italic = False
        self.font_underline = False
        self.font_color = Color.from_rgb(0, 0, 0)
        self.font_antialias = False

    def to_dict(self):
        return {
            "name": self.name,
            "text": self.text,
            "font_name": self.font_name,
            "font_size": self.font_size,
            "font_bold": self.font_bold,
            "font_italic": self.font_italic,
            "font_underline": self.font_underline,
            "font_color": self.font_color.rgba(),
            "font_antialias": self.font_antialias
        }

    @classmethod
    def from_dict(cls, game_object, values):
        comp = cls(game_object)
        comp.text = values.get("text", "")
        comp.font_name = values.get("font_name", "arial")
        comp.font_size = values.get("font_size", 16)
        comp.font_bold = values.get("font_bold", False)
        comp.font_italic = values.get("font_italic", False)
        comp.font_underline = values.get("font_underline", False)
        comp.font_color = Color.from_rgba(*values.get("font_color", (0, 0, 0, 0)))
        comp.font_antialias = values.get("font_antialias", False)
        return comp
