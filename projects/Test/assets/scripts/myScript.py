from files.scripts.script import Script


class Myscript(Script):
    def __init__(self, engine):
        super().__init__(engine, "myScript")

    def collide(self, entity):
        print(entity)
    
    def update(self):
        pos = self.entity.get_component("TransformComponent").position.copy()
        if self.engine.pg_constants.K_RIGHT in self.engine.down_keys:
            pos[0] += 1
        if self.engine.pg_constants.K_LEFT in self.engine.down_keys:
            pos[0] -= 1
        if self.engine.pg_constants.K_UP in self.engine.down_keys:
            pos[1] -= 1
        if self.engine.pg_constants.K_DOWN in self.engine.down_keys:
            pos[1] += 1
        
        if self.entity.get_component("CollisionComponent").can_go(pos):
            self.entity.get_component("TransformComponent").position = pos
