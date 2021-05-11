import json
import os


class Save:
    def __init__(self, variables, name):
        self.name = name
        self.variables = variables

    def get(self, key, default):
        return self.variables.get(key, default)

    def set(self, key, value):
        self.variables[key] = value

    def save(self):
        with open(os.path.join("saves", self.name+".json"), "w") as f:
            json.dump(self.variables, f, indent=4)

    @classmethod
    def load(cls, name):
        os.makedirs("saves")
        with open(os.path.join("saves", name+".json"), "r") as f:
            return cls(json.load(f), name)
