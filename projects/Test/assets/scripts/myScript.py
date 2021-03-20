from files.scripts.script import Script


class Myscript(Script):
    def __init__(self, engine):
        super().__init__(engine, "myScript")
    
    def update(self):
        if self.engine.pg_constants.K_RIGHT in self.engine.down_keys:
            self.entity.get_component("TransformComponent").position[0] += 1
        if self.engine.pg_constants.K_LEFT in self.engine.down_keys:
            self.entity.get_component("TransformComponent").position[0] -= 1
        if self.engine.pg_constants.K_UP in self.engine.down_keys:
            self.entity.get_component("TransformComponent").position[1] -= 1
        if self.engine.pg_constants.K_DOWN in self.engine.down_keys:
            self.entity.get_component("TransformComponent").position[1] += 1
