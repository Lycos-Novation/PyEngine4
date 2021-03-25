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
                if self.move[0] != 0 or self.move[1] != 0:
                    go = transform.position.copy()
                    go[0] += self.move[0] * deltatime
                    go[1] += self.move[1] * deltatime
                    collision = self.game_object.get_component("CollisionComponent")
                    if collision is not None:
                        if collision.can_go(go, "AUTOCOMPONENT"):
                            transform.position = go
                    else:
                        transform.position = go
                if self.rotation != 0:
                    transform.rotation += self.rotation * deltatime
