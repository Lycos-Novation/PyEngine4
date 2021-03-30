from files.scripts.script import Script


class Paddle_Script(Script):
    def __init__(self, engine):
        super().__init__(engine, "paddle_script")
    
    def update(self, deltatime):
        transform = self.game_object.get_component("TransformComponent")
        if transform.position[1] < 0:
            transform.position[1] = 0
        elif transform.position[1] > 620:
            transform.position[1] = 620
