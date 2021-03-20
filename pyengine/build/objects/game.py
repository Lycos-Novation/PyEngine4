import pygame
import pygame.locals as const

pygame.init()


class Game:
    def __init__(self, name, width, height, scenes, engine):
        self.engine = engine
        self.name = name
        self.width = width
        self.height = height
        self.scenes = scenes
        self.current_scene = 0

        pygame.display.set_caption(name)
        self.screen = pygame.display.set_mode((width, height))

        self.clock = pygame.time.Clock()
        self.is_running = False
    
    def stop(self):
        self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                if event.type == const.QUIT:
                    self.stop()
                elif event.type == const.KEYDOWN:
                    self.engine.down_keys.append(event.key)
                    self.scenes[self.current_scene].key_press(event)
                elif event.type == const.KEYUP:
                    self.engine.down_keys.remove(event.key)
                    self.scenes[self.current_scene].key_release(event)
                elif event.type == const.MOUSEBUTTONDOWN:
                    self.engine.down_mousebuttons.append(event.button)
                    self.scenes[self.current_scene].mouse_press(event)
                elif event.type == const.MOUSEBUTTONUP:
                    self.engine.down_mousebuttons.remove(event.button)
                    self.scenes[self.current_scene].mouse_release(event)
                elif event.type == const.MOUSEWHEEL:
                    self.scenes[self.current_scene].mouse_wheel(event)
                elif event.type == const.MOUSEMOTION:
                    self.scenes[self.current_scene].mouse_motion(event)

            self.scenes[self.current_scene].update()
            self.scenes[self.current_scene].show(self.screen)

            self.clock.tick()
            pygame.display.update()
