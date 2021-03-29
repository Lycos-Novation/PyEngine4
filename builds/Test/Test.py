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
    collisioncomponent = CollisionComponent(engine, True, "None")
    gameobject.add_component(collisioncomponent)
    basicphysiccomponent = BasicPhysicComponent(engine, 125)
    gameobject.add_component(basicphysiccomponent)
    controlcomponent = ControlComponent(engine, {'UPJUMP': 'K_UP', 'DOWN': 'K_DOWN', 'LEFT': 'K_LEFT', 'RIGHT': 'K_RIGHT'}, "CLASSICJUMP", 200)
    gameobject.add_component(controlcomponent)
    text = GameObject("text")
    transformcomponent = TransformComponent(engine, [20, 400], 0, [1.0, 1.0])
    text.add_component(transformcomponent)
    textcomponent = TextComponent(engine, "Hello Lyos :DDD", "arial", 50, False, False, False, [0, 0, 255, 255], True)
    text.add_component(textcomponent)
    collisioncomponent = CollisionComponent(engine, True, "None")
    text.add_component(collisioncomponent)
    sprite_sheet = GameObject("sprite_sheet")
    transformcomponent = TransformComponent(engine, [1000, 150], 0, [1.0, 1.0])
    sprite_sheet.add_component(transformcomponent)
    spritesheetcomponent = SpriteSheetComponent(engine, "sheet.png", [3, 2], 0)
    sprite_sheet.add_component(spritesheetcomponent)
    myscript = Myscript(engine)
    sprite_sheet.add_component(myscript)
    autocomponent = AutoComponent(engine, [-250, 0], 0, True)
    sprite_sheet.add_component(autocomponent)
    


    entities = [gameobject, text, sprite_sheet]
    test = Scene("test", [0, 0, 0, 0], entities)
    
    scenes = [test]

    game = Game("Test", 1080, 720, scenes, engine)
    engine.game = game
    game.run()


if __name__ == "__main__":
    launch()
