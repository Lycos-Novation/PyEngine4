import json
import os
import threading
import sys
import pygame
import shutil
import importlib

from pyengine.common.project_objects import Scene, Texture
from pyengine.build import ProjectBuilder


class Project:
    def __init__(self, name, author, icon):
        self.name = name
        self.author = author
        self.icon = icon
        self.folders = {
            "main": os.path.join("projects", self.name),
            "assets": os.path.join("projects", self.name, "assets"),
            "scripts": os.path.join("projects", self.name, "assets", "scripts"),
            "prefabs": os.path.join("projects", self.name, "assets", "prefabs"),
            "textures": os.path.join("projects", self.name, "assets", "textures"),
            "scenes": os.path.join("projects", self.name, "assets", "scenes")
        }
        self.settings = {
            "engine_version": "indev",
            "width": 1080,
            "height": 720,
            "mainScene": None,
            "editor": None
        }
        self.scenes = []
        self.textures = []
        self.scripts = []

    def get_scene(self, name):
        for i in self.scenes:
            if i.name == name:
                return i
        
    def get_texture(self, name):
        for i in self.textures:
            if i.name == name:
                return i

    def build(self):
        ProjectBuilder.build(self)

    def __launch(self):
        if os.path.exists(os.path.join("builds", self.name, self.name.title()+".py")):
            os.chdir(os.path.join("builds", self.name))
            sys.path.append(os.path.join("."))
            module = importlib.__import__(".".join(["builds", self.name, self.name.title()]))
            eval("module."+self.name+"."+self.name.title()+".launch()")
            sys.modules.pop(".".join(["builds", self.name, self.name.title()]))
            DISPLAY = (1, 1)
            DEPTH = 32
            FLAGS = 0
            pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
            os.chdir("../..")

    def launch(self):
        thread = threading.Thread(target=self.__launch)
        thread.run()

    def save(self):
        removes = [self.folders["prefabs"], self.folders["textures"], self.folders["scenes"]]
        for i in removes:
            shutil.rmtree(i, ignore_errors=True)
        if os.path.exists(os.path.join(self.folders["main"], "project.json")):
            os.remove(os.path.join(self.folders["main"], "project.json"))
        if os.path.exists(os.path.join(self.folders["main"], "settings.json")):
            os.remove(os.path.join(self.folders["main"], "settings.json"))
        for i in os.listdir(self.folders["scripts"]):
            if i.replace(".py", "") not in self.scripts:
                os.remove(os.path.join(self.folders["scripts"], i))

        for i in self.folders.values():
            os.makedirs(i, exist_ok=True)
        values = {
            "name": self.name,
            "author": self.author,
            "icon": self.icon
        }
        with open(os.path.join(self.folders["main"], "project.json"), "w") as f:
            f.write(json.dumps(values, indent=4))
        with open(os.path.join(self.folders["main"], "settings.json"), "w") as f:
            f.write(json.dumps(self.settings, indent=4))
        for i in self.scenes:
            i.save(self.folders["scenes"])
        for i in self.textures:
            i.save(self.folders["textures"])

    def __str__(self):
        return f"Project(name={self.name}, author={self.author}, icon={self.icon})"
    
    @classmethod
    def load(cls, directory):
        with open(os.path.join(directory, "project.json"), "r") as f:
            values = json.load(f)
        project = Project(
            values.get("name", "Unknown Project"),
            values.get("author", "Unknown Author"),
            values.get("icon", "default")
        )
        with open(os.path.join(directory, "settings.json"), "r") as f:
            project.settings = json.load(f)
        for i in os.listdir(project.folders["scripts"]):
            project.scripts.append(i.replace(".py", ""))
        for i in os.listdir(project.folders["scenes"]):
            project.scenes.append(Scene.load(os.path.join(project.folders["scenes"], i)))
        for i in os.listdir(project.folders["textures"]):
            project.textures.append(Texture.load(os.path.join(project.folders["textures"], i)))
        return project
