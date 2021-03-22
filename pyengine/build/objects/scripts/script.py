from files.components import Component


class Script(Component):
    def __init__(self, engine, name):
        super().__init__(engine)
        self.name = name
