from files import *
from files.components import *

def launch():
    empty = Entity("empty")
    transformcomponent = TransformComponent([150, 300], 0, [0.46, 0.46])
    spritecomponent = SpriteComponent("test.png")


    empty.add_component(transformcomponent)
    empty.add_component(spritecomponent)

    entities = [empty]
    test = Scene("test", [200, 0, 0, 0], entities)
    
    scenes = [test]

    game = Game("Test", 1080, 720, scenes)
    game.run()

if __name__ == "__main__":
    launch()