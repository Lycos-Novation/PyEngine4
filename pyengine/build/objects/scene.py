class Scene:
    def __init__(self, name, color, entities):
        self.name = name
        self.bg_color = color
        self.entities = entities

    def start(self):
        for i in self.entities:
            i.start()

    def key_press(self, evt):
        for i in self.entities:
            i.key_press(evt)

    def key_release(self, evt):
        for i in self.entities:
            i.key_release(evt)

    def mouse_press(self, evt):
        for i in self.entities:
            i.mouse_press(evt)

    def mouse_release(self, evt):
        for i in self.entities:
            i.mouse_release(evt)

    def mouse_motion(self, evt):
        for i in self.entities:
            i.mouse_motion(evt)

    def mouse_wheel(self, evt):
        for i in self.entities:
            i.mouse_wheel(evt)
    
    def update(self):
        for i in self.entities:
            i.update()

    def show(self, screen):
        screen.fill(self.bg_color)

        for i in self.entities:
            i.show(screen)
