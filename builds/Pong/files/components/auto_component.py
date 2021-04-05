from files.components.component import Component


class AutoComponent(Component):
    def __init__(self, engine, move, rotation, active):
        super().__init__(engine)
        self.name = "AutoComponent"
        self.move = move
        self.rotation = rotation
        self.active = active

    def update(self, deltatime):
        if self.active:
            transform = self.game_object.get_component("TransformComponent")
            if transform is not None:
                if self.move.x != 0 or self.move.y != 0:
                    go = transform.position
                    go.x += self.move.x * deltatime
                    go.y += self.move.y * deltatime
                    collision = self.game_object.get_component("CollisionComponent")
                    if collision is not None:
                        if collision.can_go(go, "AUTOCOMPONENT"):
                            transform.position = go
                    else:
                        transform.position = go
                if self.rotation != 0:
                    transform.rotation += self.rotation * deltatime
