class Component:
    def __init__(self, engine):
        self.game_object = None
        self.engine = engine

    def start(self):
        pass

    def update(self):
        pass

    def show(self, screen):
        pass

    def key_press(self, evt):
        pass

    def key_release(self, evt):
        pass

    def mouse_press(self, evt):
        pass

    def mouse_release(self, evt):
        pass

    def mouse_motion(self, evt):
        pass

    def mouse_wheel(self, evt):
        pass
