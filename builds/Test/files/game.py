import pygame
import pygame.locals as const

pygame.init()


class Game:
    def __init__(self, name, width, height, scenes):
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
            
            self.scenes[self.current_scene].update()
            self.scenes[self.current_scene].show(self.screen)
            

            self.clock.tick()
            pygame.display.update()