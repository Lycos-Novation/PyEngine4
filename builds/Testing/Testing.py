from files import *
from files.components import *
from files.scripts import *
from files.utils import *


def launch():
    engine = Engine("en")

    e1 = GameObject("e1", "Object", 1)
    transformcomponent = TransformComponent(engine, Vec2(100, 100), 0, Vec2(1.0, 1.0))
    e1.add_component(transformcomponent)
    spritecomponent = SpriteComponent(engine, "e1.png")
    e1.add_component(spritecomponent)
    controlcomponent = ControlComponent(engine, {'UPJUMP': 'K_UP', 'DOWN': 'K_DOWN', 'LEFT': 'K_LEFT', 'RIGHT': 'K_RIGHT'}, "FOURDIRECTION", 200)
    e1.add_component(controlcomponent)
    particlecomponent = ParticleComponent(engine, Color.from_rgba(255, 255, 255, 255), Color.from_rgba(0, 0, 0, 255), Vec2(20, 20), Vec2(0, 0), Vec2(0, 359), Vec2(0, 0), Vec2(10, 10), Vec2(10, 10), 1, 0.01, 10)
    e1.add_component(particlecomponent)
    collisioncomponent = CollisionComponent(engine, True, "None", Vec2(20, 20))
    e1.add_component(collisioncomponent)

    e2 = GameObject("e2", "Object", 0)
    transformcomponent = TransformComponent(engine, Vec2(250, 300), 0, Vec2(1.0, 1.0))
    e2.add_component(transformcomponent)
    spritecomponent = SpriteComponent(engine, "e2.png")
    e2.add_component(spritecomponent)
    collisioncomponent = CollisionComponent(engine, True, "None", Vec2(10, 100))
    e2.add_component(collisioncomponent)

    button = GameObject("button", "Object", 0)
    transformcomponent = TransformComponent(engine, Vec2(970, 10), 0, Vec2(1.0, 1.0))
    button.add_component(transformcomponent)
    buttoncomponent = ButtonComponent(engine, Color.from_rgba(255, 0, 0, 255), Vec2(100, 40), "printLang - clicked", "Print", "arial", 20, True, False, True, Color.from_rgba(255, 255, 255, 255), True)
    button.add_component(buttoncomponent)
    printlang = Printlang(engine)
    button.add_component(printlang)
    
    entities = [e1, e2, button]
    base = Scene(engine, "base", Color.from_rgba(0, 0, 0, 255), 1, Vec2(0, 0), e1, entities)
    
    scenes = [base]
    game = Game("Testing", 1080, 720, 8, True, scenes, engine)
    game.run()


if __name__ == "__main__":
    launch()
