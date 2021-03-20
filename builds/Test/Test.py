from files import *
from files.components import *
from files.scripts import *


def launch():
    engine = Engine()
    gameobject = Entity("gameobject")
    transformcomponent = TransformComponent(engine, [0, 0], 0, [1, 1])
    spritecomponent = SpriteComponent(engine, "test.png")
    myscript = Myscript(engine)


    gameobject.add_component(transformcomponent)
    gameobject.add_component(spritecomponent)
    gameobject.add_component(myscript)

    entities = [gameobject]
    test = Scene("test", [0, 0, 0, 0], entities)
    
    scenes = [test]

    game = Game("Test", 1080, 720, scenes, engine)
    engine.game = game
    game.run()


if __name__ == "__main__":
    launch()
