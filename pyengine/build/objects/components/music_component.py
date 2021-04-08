from files.components.component import Component

import pygame
import os


class MusicComponent(Component):
    def __init__(self, engine, music, volume, play, loop):
        super().__init__(engine)
        self.name = "MusicComponent"
        self.__music = os.path.join("resources", "sounds", music)
        self.__volume = volume
        self.__play = play
        self.loop = loop

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value
        pygame.mixer.music.set_volume(value/100)

    @property
    def play(self):
        return self.__play

    @play.setter
    def play(self, value):
        self.__play = value
        if value:
            if self.loop:
                pygame.mixer.music.play(loops=-1)
            else:
                pygame.mixer.music.play()
        else:
            pygame.mixer.music.stop()

    @property
    def music(self):
        return os.path.basename(self.__music)

    @music.setter
    def music(self, value):
        self.__music = os.path.join("resources", "sounds", value)
        pygame.mixer.music.load(self.__music)

    def start(self):
        self.music = self.music
        self.play = self.play
