import pygame


class Entity:
    def __init__(self, name):
        self.name = name
        self.childs = []
        self.components = []

    def add_component(self, comp):
        self.components.append(comp)
        comp.entity = self

    def get_component(self, name):
        for i in self.components:
            if i.name == name:
                return i
    
    def update(self):
        for i in self.components:
            i.update()

    def show(self, screen):
        for i in self.components:
            i.show(screen)