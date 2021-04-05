from files.scripts.script import Script
from files.utils import clamp


class Paddle_Script(Script):
    def __init__(self, engine):
        super().__init__(engine, "paddle_script")
    
    def update(self, deltatime):
        transform = self.game_object.get_component("TransformComponent")
        transform.position.y = clamp(transform.position.y, 0, 620)
