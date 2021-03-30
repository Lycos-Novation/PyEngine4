from files.components.component import Component


class BasicPhysicComponent(Component):
    def __init__(self, engine, gravity):
        super().__init__(engine)
        self.name = "BasicPhysicComponent"
        self.gravity = gravity
        self.max_gravity = gravity
        self.grounded = False
        self.time = 0.0025

    def update(self, deltatime):
        transform = self.game_object.get_component("TransformComponent")
        if transform is not None:
            pos = transform.position.copy()
            pos[1] += self.gravity * deltatime

            collision = self.game_object.get_component("CollisionComponent")
            if collision is not None:
                if collision.can_go(pos, "GRAVITY"):
                    self.grounded = False
                    transform.position = pos
                elif self.gravity > 0:
                    self.grounded = True
                    self.gravity = 2
            else:
                transform.position = pos

            if self.time <= 0 and self.gravity < self.max_gravity and not self.grounded:
                self.gravity += 1
                self.time = 0.0025
            self.time -= deltatime
