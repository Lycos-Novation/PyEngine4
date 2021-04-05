import pygame
import pygame.locals as const

pygame.init()


class Game:
    def __init__(self, title, width, height, scenes, engine):
        self.engine = engine
        self.engine.game = self
        self.title = title
        self.__width = width
        self.__height = height
        self.scenes = scenes
        self.current_scene = 0

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        self.is_running = False

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        self.screen = pygame.display.set_mode((self.__width, self.height))

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        self.screen = pygame.display.set_mode((self.width, self.__height))

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title
        pygame.display.set_caption(title)
    
    def stop(self):
        self.is_running = False

    def get_fps(self):
        return self.clock.get_fps()

    def run(self):
        self.is_running = True
        self.scenes[self.current_scene].start()
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

            self.scenes[self.current_scene].update(self.clock.get_time() / 1000)
            self.scenes[self.current_scene].show(self.screen)

            self.clock.tick()
            pygame.display.update()
