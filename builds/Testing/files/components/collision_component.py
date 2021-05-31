import pygame
from files.components.component import Component


class CollisionComponent(Component):
    def __init__(self, engine, solid, callback, size):
        super().__init__(engine)
        self.name = "CollisionComponent"
        self.solid = solid
        if callback == "None":
            self.callback = None
        else:
            self.callback = callback
        self.size = size

    def __rect_collide(self, rect1, rect2, game_object, cause, e_collision):
        if rect1.colliderect(rect2):
            if self.callback is not None:
                names = self.callback.split(" - ")
                eval('self.game_object.get_component("' + names[0] + '").' + names[1] + "(game_object, cause)")
            if e_collision.solid and self.solid:
                return True
        return False

    def __internal_collide(self, rect, cause):
        for game_object in self.engine.get_current_scene().game_objects:
            if game_object != self.game_object:
                e_transform = game_object.get_component("TransformComponent")
                e_collision = game_object.get_component("CollisionComponent")
                if e_collision is not None and e_transform is not None:
                    e_pos = e_transform.position
                    e_rect = pygame.Rect((e_pos - e_collision.size / 2).coords(), e_collision.size.coords())
                    if self.__rect_collide(rect, e_rect, game_object, cause, e_collision):
                        return True
        return False

    def can_go(self, position, cause="UNKNOWN"):
        transform = self.game_object.get_component("TransformComponent")
        if transform is not None:
            rect = pygame.Rect((position - self.size / 2).coords(), self.size.coords())
            if self.__internal_collide(rect, cause):
                return False
        return True
