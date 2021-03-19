from files.components.component import Component


class TransformComponent(Component):
    def __init__(self, position, rotation, scale):
        super().__init__()
        self.name = "TransformComponent"
        self.position = position
        self.rotation = rotation
        self.scale = scale