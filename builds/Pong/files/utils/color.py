class Color:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.a = 255

    def darker(self, force=1):
        if force < 1:
            force = 1
        result = []
        for i in self.rgb():
            result.append(i - 10*force)
            if result[-1] < 0:
                result[-1] = 0
        return Color.from_rgba(*result, self.a)

    def lighter(self, force=1):
        if force < 1:
            force = 1
        result = []
        for i in self.rgb():
            result.append(i + 10*force)
            if result[-1] < 0:
                result[-1] = 0
        return Color.from_rgba(*result, self.a)

    def rgb(self):
        return self.r, self.g, self.b

    def rgba(self):
        return self.r, self.g, self.b, self.a

    def html(self):
        return ("#" + hex(self.r)[2:] + hex(self.g)[2:] + hex(self.b)[2:] + hex(self.a)[2:]).upper()

    def __repr__(self):
        return "Color.from_rgba"+str(self.rgba())

    @classmethod
    def from_rgb(cls, r, g, b):
        color = cls()
        color.r = r
        color.g = g
        color.b = b
        return color

    @classmethod
    def from_rgba(cls, r, g, b, a):
        color = cls.from_rgb(r, g, b)
        color.a = a
        return color

    @classmethod
    def from_color(cls, color):
        return cls.from_rgba(*color.rgba())

    @classmethod
    def from_html(cls, html):
        if len(html) == 7 or len(html) == 9:
            if len(html) == 7:
                html += "FF"
            return cls.from_rgba(*(int(html[1:3], 16), int(html[3:5], 16), int(html[5:7], 16), int(html[7:9], 16)))

    @classmethod
    def from_name(cls, name):
        colors = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "GRAY": (128, 128, 128),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0),
            "BLUE": (0, 0, 255),
            "FUCHSIA": (255, 0, 255),
            "YELLOW": (255, 255, 0),
            "CYAN": (0, 255, 255),
            "LIME": (0, 128, 0),
            "BROWN": (128, 0, 0),
            "NAVY_BLUE": (0, 0, 128),
            "OLIVE": (128, 128, 0),
            "PURPLE": (128, 0, 128),
            "TEAL": (0, 128, 128),
            "SILVER": (192, 192, 192),
            "ORANGE": (255, 128, 0)
        }
        return cls.from_rgb(*colors[name])
