from files.scripts.script import Script


class Myscript(Script):
    def __init__(self, engine):
        super().__init__(engine, "myScript")
    
    def update(self):
        pos = self.entity.get_component("TransformComponent").position.copy()
        phys = self.entity.get_component("BasicPhysicComponent")
        if self.engine.pg_constants.K_RIGHT in self.engine.down_keys:
            pos[0] += 6
        if self.engine.pg_constants.K_LEFT in self.engine.down_keys:
            pos[0] -= 6
        if self.engine.pg_constants.K_UP in self.engine.down_keys and phys.grounded:
            phys.gravity = -5
        
        if self.entity.get_component("CollisionComponent").can_go(pos, "MyScript"):
            self.entity.get_component("TransformComponent").position = pos
