import pygame.locals


class Engine:
    def __init__(self):
        self.game = None
        self.pg_constants = pygame.locals
        self.down_keys = []
        self.down_mousebuttons = []

    def stop_game(self):
        self.game.stop()
