from files.components.component import Component


class CollisionComponent(Component):
    def __init__(self, engine, solid, callback):
        super().__init__(engine)
        self.name = "CollisionComponent"
        self.solid = solid
        if callback == "None":
            self.callback = None
        else:
            self.callback = callback

    def __rect_collide(self, rect1, rect2, entity, cause, e_collision):
        if rect1.colliderect(rect2):
            if self.callback is not None:
                names = self.callback.split(" - ")
                eval('self.entity.get_component("' + names[0] + '").' + names[1] + "(entity, cause)")
            if e_collision.solid and self.solid:
                return True
        return False

    def __internal_collide(self, rect, cause):
        for entity in self.engine.get_current_scene().entities:
            if entity != self.entity:
                e_transform = entity.get_component("TransformComponent")
                e_sprite = entity.get_component("SpriteComponent")
                e_text = entity.get_component("TextComponent")
                e_collision = entity.get_component("CollisionComponent")
                if e_collision is not None and e_transform is not None:
                    e_pos = e_transform.position
                    if e_sprite is not None:
                        e_rect = e_sprite.render.get_rect(x=e_pos[0], y=e_pos[1])
                        if self.__rect_collide(rect, e_rect, entity, cause, e_collision):
                            return True

                    if e_text is not None:
                        e_rect = e_text.render.get_rect(x=e_pos[0], y=e_pos[1])
                        if self.__rect_collide(rect, e_rect, entity, cause, e_collision):
                            return True
        return False

    def can_go(self, position, cause="UNKNOWN"):
        transform = self.entity.get_component("TransformComponent")
        sprite = self.entity.get_component("SpriteComponent")
        text = self.entity.get_component("TextComponent")
        if transform is not None:
            if sprite is not None:
                rect = sprite.render.get_rect(x=position[0], y=position[1])
                if self.__internal_collide(rect, cause):
                    return False
            if text is not None:
                rect = text.render.get_rect(x=position[0], y=position[1])
                if self.__internal_collide(rect, cause):
                    return False
        return True
