from files.components.component import Component


class ControlComponent(Component):
    def __init__(self, engine, keys, type_, speed):
        super().__init__(engine)
        self.name = "TransformComponent"
        self.keys = keys
        self.control_type = type_
        self.speed = speed

    def update(self, deltatime):
        for i in self.engine.down_keys:
            self.move_by_key(i, deltatime)

    def move_by_key(self, key, deltatime):
        transform = self.game_object.get_component("TransformComponent")
        if transform is not None:
            position = transform.position.copy()
            cause = "UNKNOWN"
            if key == eval("self.engine.pg_constants."+self.keys["UPJUMP"]):
                if self.control_type in ("FOURDIRECTION", "DOWNUP"):
                    position[1] -= self.speed*deltatime
                    cause = "UPCONTROL"
                elif self.control_type == "CLASSICJUMP":
                    phys = self.game_object.get_component("BasicPhysicComponent")
                    if phys.grounded:
                        phys.gravity = -phys.max_gravity
            elif key == eval("self.engine.pg_constants."+self.keys["DOWN"]):
                if self.control_type in ("FOURDIRECTION", "DOWNUP"):
                    position[1] += self.speed*deltatime
                    cause = "DOWNCONTROL"
            elif key == eval("self.engine.pg_constants."+self.keys["RIGHT"]):
                if self.control_type in ("FOURDIRECTION", "LEFTRIGHT", "CLASSICJUMP"):
                    position[0] += self.speed*deltatime
                    cause = "RIGHTCONTROL"
            elif key == eval("self.engine.pg_constants."+self.keys["LEFT"]):
                if self.control_type in ("FOURDIRECTION", "LEFTRIGHT", "CLASSICJUMP"):
                    position[0] -= self.speed*deltatime
                    cause = "LEFTCONTROL"

            if position != transform.position:
                collision = self.game_object.get_component("CollisionComponent")
                if collision is None:
                    transform.position = position
                else:
                    if collision.can_go(position, cause):
                        transform.position = position
