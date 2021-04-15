from files.components.component import Component

import pygame
import os


class SoundComponent(Component):
    def __init__(self, engine, sound, volume):
        super().__init__(engine)

        if sound == "None":
            sound = None

        self.name = "SoundComponent"

        self.sound = sound
        self.volume = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def play(self):
        if self.__sound is not None:
            sound = pygame.mixer.Sound(self.__sound)
            sound.set_volume(self.volume / 100)
            sound.play()

    @property
    def sound(self):
        if self.__sound is None:
            return None
        return os.path.basename(self.__sound)

    @sound.setter
    def sound(self, value):
        if value is not None:
            self.__sound = os.path.join("resources", "sounds", value)
        else:
            self.__sound = None
