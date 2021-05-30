import pygame.locals
import os

from files.utils import Vec2
from files.utils.settings import Settings
from files.utils.lang import LangManager


class Engine:
    def __init__(self, default_lang):
        self.game = None
        self.pg_constants = pygame.locals
        self.down_keys = []
        self.down_mousebuttons = []
        self.settings = Settings()
        self.lang_manager = LangManager()
        for i in os.listdir(os.path.join("resources", "langs")):
            self.lang_manager.add_lang(i.replace(".json", ""), os.path.join("resources", "langs", i))
        self.lang_manager.change_lang(default_lang)

    def get_game_size(self):
        return Vec2(self.game.width, self.game.height)

    def get_game_object(self, id_):
        return self.game.scenes[self.game.current_scene].get_game_object(id_)

    def get_current_scene(self):
        return self.game.scenes[self.game.current_scene]

    def stop_game(self):
        self.game.stop()
