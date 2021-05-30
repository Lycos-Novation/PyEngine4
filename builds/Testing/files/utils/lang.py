import json
import os


class Lang:
    def __init__(self, file):
        self.file = file

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.translations = {}
        self.__file = file
        if os.path.exists(file):
            with open(file, "r") as f:
                self.translations = json.load(f)

    def get_translate(self, key, default, *args):
        return self.translations.get(key, default).format(*args)


class LangManager:
    def __init__(self):
        self.langs = {}
        self.current_lang = None

    def add_lang(self, name, file):
        if name in self.langs.keys():
            return False
        self.langs[name] = Lang(file)
        return True

    def remove_lang(self, name):
        if name in self.langs.keys():
            del self.langs[name]
            return True
        return False

    def get_translate(self, key, default, *args):
        if self.current_lang is not None:
            return self.langs[self.current_lang].get_translate(key, default, *args)
        return default

    def change_lang(self, name):
        if name in self.langs.keys():
            self.current_lang = name
            return True
        return False

    def get_langs(self):
        return self.langs.keys()
