from files import *
from files.components import *
from files.scripts import *
from files.utils import *


def launch():
    engine = Engine()

    e1 = GameObject("e1", "Object", -1)
    transformcomponent = TransformComponent(engine, Vec2(100, 100), 0, Vec2(1.0, 1.0))
    e1.add_component(transformcomponent)
    spritecomponent = SpriteComponent(engine, "e1.png")
    e1.add_component(spritecomponent)
    controlcomponent = ControlComponent(engine, {'UPJUMP': 'K_UP', 'LEFT': 'K_LEFT', 'RIGHT': 'K_RIGHT', 'DOWN': 'K_DOWN'}, "FOURDIRECTION", 200)
    e1.add_component(controlcomponent)

    e2 = GameObject("e2", "Object", 0)
    transformcomponent = TransformComponent(engine, Vec2(250, 300), 0, Vec2(1.0, 1.0))
    e2.add_component(transformcomponent)
    spritecomponent = SpriteComponent(engine, "e2.png")
    e2.add_component(spritecomponent)
    
    entities = [e1, e2]
    base = Scene("base", Color.from_rgba(0, 0, 0, 255), 1, Vec2(0, 0), entities)
    
    scenes = [base]
    game = Game("Testing", 1080, 720, 8, scenes, engine)
    game.run()


if __name__ == "__main__":
    launch()
