import pygame.locals


class Engine:
    def __init__(self):
        self.game = None
        self.pg_constants = pygame.locals
        self.down_keys = []
        self.down_mousebuttons = []

    def get_game_object(self, id_):
        return self.game.scenes[self.game.current_scene].get_game_object(id_)

    def get_current_scene(self):
        return self.game.scenes[self.game.current_scene]

    def stop_game(self):
        self.game.stop()
