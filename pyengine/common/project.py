import json
import os
import threading
import sys
import pygame
import shutil
import importlib

from pyengine.common.project_objects import Scene, Texture, Sound
from pyengine.build import ProjectBuilder
from pyengine.common.utils import core_logger
from pyengine import common

from types import ModuleType


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
            "scenes": os.path.join("projects", self.name, "assets", "scenes"),
            "sounds": os.path.join("projects", self.name, "assets", "sounds")
        }
        self.settings = {
            "engine_version": common.__version__,
            "width": 1080,
            "height": 720,
            "mainScene": None
        }
        self.scenes = []
        self.textures = []
        self.sounds = []
        self.scripts = []
        self.crash = False
        self.module = None

    def get_scene(self, name):
        for i in self.scenes:
            if i.name == name:
                return i
        
    def get_texture(self, name):
        for i in self.textures:
            if i.name == name:
                return i

    def get_sound(self, name):
        for i in self.sounds:
            if i.name == name:
                return i

    def build(self):
        ProjectBuilder.build(self)

    def __reload_module(self, module=None, mdict=None):
        if module is None:
            module = self.module
        if mdict is None:
            mdict = {}
        if module not in mdict:
            mdict[module] = []
        importlib.reload(module)
        for name in dir(module):
            attr = getattr(module, name)
            if type(attr) is ModuleType:
                if attr not in mdict[module]:
                    if attr.__name__ not in sys.builtin_module_names and attr.__name__ not in ["pygame", "pygame.color",
                                                                                               "pygame.locals"]:
                        mdict[module].append(attr)
                        self.__reload_module(attr, mdict)
        importlib.reload(module)  # NEEDED FOR SOME MODULES

    def __launch(self):
        self.crash = False
        if os.path.exists(os.path.join("builds", self.name, self.name.title()+".py")):
            sys.path.append(os.path.join("builds", self.name))
            if self.module is None:
                self.module = importlib.__import__("Pong")
            else:
                self.__reload_module()
            os.chdir(os.path.join("builds", self.name))
            try:
                self.module.launch()
            except Exception as e:
                self.crash = True
                core_logger.exception("Error in Game Launching")
            DISPLAY = (1, 1)
            DEPTH = 32
            FLAGS = 0
            pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
            os.chdir("../..")

    def launch(self):
        thread = threading.Thread(target=self.__launch)
        thread.run()
        return self.crash

    def save(self):
        self.settings["engine_version"] = common.__version__

        removes = [self.folders["prefabs"], self.folders["textures"], self.folders["sounds"], self.folders["scenes"]]
        for i in removes:
            shutil.rmtree(i, ignore_errors=True)
        if os.path.exists(os.path.join(self.folders["main"], "project.json")):
            os.remove(os.path.join(self.folders["main"], "project.json"))
        if os.path.exists(os.path.join(self.folders["main"], "settings.json")):
            os.remove(os.path.join(self.folders["main"], "settings.json"))
        if os.path.exists(self.folders["scripts"]):
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
        for i in self.sounds:
            i.save(self.folders["sounds"])

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
        for i in project.folders.values():
            os.makedirs(i, exist_ok=True)

        with open(os.path.join(directory, "settings.json"), "r") as f:
            project.settings = json.load(f)
        for i in os.listdir(project.folders["scripts"]):
            project.scripts.append(i.replace(".py", ""))
        for i in os.listdir(project.folders["scenes"]):
            project.scenes.append(Scene.load(os.path.join(project.folders["scenes"], i)))
        for i in os.listdir(project.folders["textures"]):
            project.textures.append(Texture.load(os.path.join(project.folders["textures"], i)))
        for i in os.listdir(project.folders["sounds"]):
            project.sounds.append(Sound.load(os.path.join(project.folders["sounds"], i)))
        return project
