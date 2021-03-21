from files import *
from files.components import *
from files.scripts import *


def launch():
    engine = Engine()
    gameobject = GameObject("gameobject")
    transformcomponent = TransformComponent(engine, [100, 200], 0, [1.0, 1.0])
    gameobject.add_component(transformcomponent)
    spritecomponent = SpriteComponent(engine, "test.png")
    gameobject.add_component(spritecomponent)
    myscript = Myscript(engine)
    gameobject.add_component(myscript)
    collisioncomponent = CollisionComponent(engine, True, "myScript - collide")
    gameobject.add_component(collisioncomponent)
    text = GameObject("text")
    transformcomponent = TransformComponent(engine, [300, 200], 0, [1.0, 1.0])
    text.add_component(transformcomponent)
    textcomponent = TextComponent(engine, "Hello Lyos :DDD", "arial", 50, False, False, False, [0, 0, 255, 255], True)
    text.add_component(textcomponent)
    collisioncomponent = CollisionComponent(engine, True, "None")
    text.add_component(collisioncomponent)
    

    entities = [gameobject, text]
    test = Scene("test", [0, 0, 0, 0], entities)
    
    scenes = [test]

    game = Game("Test", 1080, 720, scenes, engine)
    engine.game = game
    game.run()


if __name__ == "__main__":
    launch()
