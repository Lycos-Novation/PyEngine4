class ScriptComponent:
    def __init__(self):
        self.name = "ScriptComponent "

    def to_dict(self):
        return {
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, values):
        comp = ScriptComponent()
        comp.name = values.get("name", "")
        return comp
