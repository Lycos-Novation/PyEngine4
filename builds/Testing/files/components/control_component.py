from files.components.component import Component

import copy


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
            position = copy.copy(transform.position)
            cause = "UNKNOWN"
            for i in self.keys["UPJUMP"].split(" "):
                if key == eval("self.engine.pg_constants."+i):
                    if self.control_type in ("FOURDIRECTION", "UPDOWN"):
                        position.y -= self.speed*deltatime
                        cause = "UPCONTROL"
                    elif self.control_type == "CLASSICJUMP":
                        phys = self.game_object.get_component("BasicPhysicComponent")
                        if phys.grounded:
                            phys.gravity = -phys.max_gravity
                    break

            for i in self.keys["DOWN"].split(" "):
                if key == eval("self.engine.pg_constants."+i):
                    if self.control_type in ("FOURDIRECTION", "UPDOWN"):
                        position.y += self.speed*deltatime
                        cause = "DOWNCONTROL"
                    break

            for i in self.keys["RIGHT"].split(" "):
                if key == eval("self.engine.pg_constants."+i):
                    if self.control_type in ("FOURDIRECTION", "LEFTRIGHT", "CLASSICJUMP"):
                        position.x += self.speed*deltatime
                        cause = "RIGHTCONTROL"
                    break

            for i in self.keys["LEFT"].split(" "):
                if key == eval("self.engine.pg_constants."+i):
                    if self.control_type in ("FOURDIRECTION", "LEFTRIGHT", "CLASSICJUMP"):
                        position.x -= self.speed*deltatime
                        cause = "LEFTCONTROL"
                    break

            print(position, transform.position)

            if position != transform.position:
                print("CHEH")
                collision = self.game_object.get_component("CollisionComponent")
                if collision is None:
                    print("NOT VERIFY CAN GO")
                    transform.position = position
                else:
                    print("VERIFY CAN GO")
                    if collision.can_go(position, cause):
                        transform.position = position
