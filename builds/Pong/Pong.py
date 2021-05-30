from files import *
from files.components import *
from files.scripts import *
from files.utils import *


def launch():
    engine = Engine("None")

    left_paddle = GameObject("left_paddle", "Object", 0)
    transformcomponent = TransformComponent(engine, Vec2(50, 310), 0, Vec2(1.0, 1.0))
    left_paddle.add_component(transformcomponent)
    spritecomponent = SpriteComponent(engine, "paddle.png")
    left_paddle.add_component(spritecomponent)
    collisioncomponent = CollisionComponent(engine, True, "None", Vec2(10, 100))
    left_paddle.add_component(collisioncomponent)
    controlcomponent = ControlComponent(engine, {'UPJUMP': 'K_a', 'DOWN': 'K_q', 'LEFT': 'K_LEFT', 'RIGHT': 'K_RIGHT'}, "UPDOWN", 200)
    left_paddle.add_component(controlcomponent)
    paddle_script = Paddle_Script(engine)
    left_paddle.add_component(paddle_script)

    right_paddle = GameObject("right_paddle", "Object", 0)
    transformcomponent = TransformComponent(engine, Vec2(1020, 310), 0, Vec2(1.0, 1.0))
    right_paddle.add_component(transformcomponent)
    spritecomponent = SpriteComponent(engine, "paddle.png")
    right_paddle.add_component(spritecomponent)
    collisioncomponent = CollisionComponent(engine, True, "None", Vec2(10, 100))
    right_paddle.add_component(collisioncomponent)
    controlcomponent = ControlComponent(engine, {'UPJUMP': 'K_UP', 'DOWN': 'K_DOWN', 'LEFT': 'K_LEFT', 'RIGHT': 'K_RIGHT'}, "UPDOWN", 200)
    right_paddle.add_component(controlcomponent)
    paddle_script = Paddle_Script(engine)
    right_paddle.add_component(paddle_script)

    score = GameObject("score", "Object", 0)
    transformcomponent = TransformComponent(engine, Vec2(10, 10), 0, Vec2(1.0, 1.0))
    score.add_component(transformcomponent)
    textcomponent = TextComponent(engine, "P1 : 0 - P2 : 0", "arial", 20, True, False, False, Color.from_rgba(255, 255, 255, 255), True)
    score.add_component(textcomponent)

    ball = GameObject("ball", "Object", 0)
    transformcomponent = TransformComponent(engine, Vec2(530, 350), 0, Vec2(1.0, 1.0))
    ball.add_component(transformcomponent)
    spritecomponent = SpriteComponent(engine, "ball.png")
    ball.add_component(spritecomponent)
    collisioncomponent = CollisionComponent(engine, True, "ball_script - collide", Vec2(20, 20))
    ball.add_component(collisioncomponent)
    autocomponent = AutoComponent(engine, Vec2(200, 157), 0, True)
    ball.add_component(autocomponent)
    ball_script = Ball_Script(engine)
    ball.add_component(ball_script)

    quit_button = GameObject("quit_button", "Object", 0)
    transformcomponent = TransformComponent(engine, Vec2(965, 10), 0, Vec2(1.0, 1.0))
    quit_button.add_component(transformcomponent)
    buttoncomponent = ButtonComponent(engine, Color.from_rgba(241, 241, 241, 255), Vec2(100, 40), "quit_script - click", "Quitter", "arial", 20, False, False, False, Color.from_rgba(255, 0, 4, 255), True)
    quit_button.add_component(buttoncomponent)
    quit_script = Quit_Script(engine)
    quit_button.add_component(quit_script)
    soundcomponent = SoundComponent(engine, "music.mp3", 100)
    quit_button.add_component(soundcomponent)
    
    entities = [left_paddle, right_paddle, score, ball, quit_button]
    game = Scene(engine, "game", Color.from_rgba(0, 0, 0, 255), 1.0, Vec2(0, 0), None, entities)
    
    scenes = [game]
    game = Game("Pong", 1080, 720, 10, scenes, engine)
    game.run()


if __name__ == "__main__":
    launch()
