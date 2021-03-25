class GameObject:
    def __init__(self, name):
        self.name = name
        self.childs = []
        self.components = []
        self.id_ = -1

    def add_component(self, comp):
        self.components.append(comp)
        comp.game_object = self

    def get_component(self, name):
        for i in self.components:
            if i.name == name:
                return i

    def start(self):
        for i in self.components:
            i.start()

    def key_press(self, evt):
        for i in self.components:
            i.key_press(evt)

    def key_release(self, evt):
        for i in self.components:
            i.key_release(evt)

    def mouse_press(self, evt):
        for i in self.components:
            i.mouse_press(evt)

    def mouse_release(self, evt):
        for i in self.components:
            i.mouse_release(evt)

    def mouse_motion(self, evt):
        for i in self.components:
            i.mouse_motion(evt)

    def mouse_wheel(self, evt):
        for i in self.components:
            i.mouse_wheel(evt)

    def update(self, deltatime):
        for i in self.components:
            i.update(deltatime)

    def show(self, screen):
        for i in self.components:
            i.show(screen)
