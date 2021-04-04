import json
import os


class EngineSettings:
    def __init__(self):
        with open(os.path.join("pyengine", "resources", "settings.json"), "r") as f:
            self.values = json.load(f)

    def save(self):
        with open(os.path.join("pyengine", "resources", "settings.json"), "w") as f:
            f.write(json.dumps(self.values, indent=4))
