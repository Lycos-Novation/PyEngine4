from files.components.component import Component


class TransformComponent(Component):
    def __init__(self, engine, position, rotation, scale):
        super().__init__(engine)
        self.name = "TransformComponent"
        self.position = position
        self.rotation = rotation
        self.scale = scale
