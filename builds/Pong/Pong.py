from files import *
from files.components import *
from files.scripts import *


def launch():
    engine = Engine()
    left_paddle = GameObject("left_paddle")
    transformcomponent = TransformComponent(engine, [50, 310], 0, [1.0, 1.0])
    left_paddle.add_component(transformcomponent)
    spritecomponent = SpriteComponent(engine, "paddle.png")
    left_paddle.add_component(spritecomponent)
    collisioncomponent = CollisionComponent(engine, True, "None")
    left_paddle.add_component(collisioncomponent)
    controlcomponent = ControlComponent(engine, {'UPJUMP': 'K_a', 'DOWN': 'K_q', 'LEFT': 'K_LEFT', 'RIGHT': 'K_RIGHT'}, "UPDOWN", 200)
    left_paddle.add_component(controlcomponent)
    paddle_script = Paddle_Script(engine)
    left_paddle.add_component(paddle_script)
    right_paddle = GameObject("right_paddle")
    transformcomponent = TransformComponent(engine, [1020, 310], 0, [1.0, 1.0])
    right_paddle.add_component(transformcomponent)
    spritecomponent = SpriteComponent(engine, "paddle.png")
    right_paddle.add_component(spritecomponent)
    collisioncomponent = CollisionComponent(engine, True, "None")
    right_paddle.add_component(collisioncomponent)
    controlcomponent = ControlComponent(engine, {'UPJUMP': 'K_UP', 'DOWN': 'K_DOWN', 'LEFT': 'K_LEFT', 'RIGHT': 'K_RIGHT'}, "UPDOWN", 200)
    right_paddle.add_component(controlcomponent)
    paddle_script = Paddle_Script(engine)
    right_paddle.add_component(paddle_script)
    score = GameObject("score")
    transformcomponent = TransformComponent(engine, [10, 10], 0, [1.0, 1.0])
    score.add_component(transformcomponent)
    textcomponent = TextComponent(engine, "P1 : 0 - P2 : 0", "arial", 20, True, False, False, [255, 255, 255, 255], True)
    score.add_component(textcomponent)
    ball = GameObject("ball")
    transformcomponent = TransformComponent(engine, [530, 350], 0, [1.0, 1.0])
    ball.add_component(transformcomponent)
    spritecomponent = SpriteComponent(engine, "ball.png")
    ball.add_component(spritecomponent)
    collisioncomponent = CollisionComponent(engine, True, "ball_script - collide")
    ball.add_component(collisioncomponent)
    autocomponent = AutoComponent(engine, [200, 157], 0, True)
    ball.add_component(autocomponent)
    ball_script = Ball_Script(engine)
    ball.add_component(ball_script)
    



    entities = [left_paddle, right_paddle, score, ball]
    game = Scene("game", [0, 0, 0, 255], entities)
    
    scenes = [game]

    game = Game("Pong", 1080, 720, scenes, engine)
    engine.game = game
    game.run()


if __name__ == "__main__":
    launch()
