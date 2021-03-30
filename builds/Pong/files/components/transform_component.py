from files.components.component import Component


class TransformComponent(Component):
    def __init__(self, engine, position, rotation, scale):
        super().__init__(engine)
        self.name = "TransformComponent"
        self.__rotation = rotation
        self.__scale = scale
        self.position = position

    def global_position(self):
        position = self.position.copy()
        if self.game_object.parent is not None:
            if self.game_object.parent.get_component("TransformComponent") is not None:
                pposition = self.game_object.parent.get_component("TransformComponent").global_position()
                position[0] += pposition[0]
                position[1] += pposition[1]
        return position

    def global_rotation(self):
        rotation = self.rotation
        if self.game_object.parent is not None:
            if self.game_object.parent.get_component("TransformComponent") is not None:
                rotation += self.game_object.parent.get_component("TransformComponent").rotation
        return rotation

    def global_scale(self):
        scale = self.scale.copy()
        if self.game_object.parent is not None:
            if self.game_object.parent.get_component("TransformComponent") is not None:
                pscale = self.game_object.parent.get_component("TransformComponent").global_scale()
                scale[0] += pscale[0]
                scale[1] += pscale[1]
        return scale

    def __update_render(self):
        sprite = self.game_object.get_component("SpriteComponent")
        text = self.game_object.get_component("TextComponent")
        spritesheet = self.game_object.get_component("SpriteSheetComponent")
        if sprite is not None:
            sprite.update_render()
        if text is not None:
            text.update_render()
        if spritesheet is not None:
            spritesheet.update_render()

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, value):
        self.__rotation = value
        self.__update_render()

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, value):
        self.__scale = value
        self.__update_render()
