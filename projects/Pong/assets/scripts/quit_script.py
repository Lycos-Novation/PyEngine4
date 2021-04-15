from files.scripts.script import Script


class Quit_Script(Script):
    def __init__(self, engine):
        super().__init__(engine, "quit_script")
    
    def click(self):
        self.engine.game.title = "MEGA PONG !"
        self.engine.game.width = 800
        self.engine.game.height = 600
        self.game_object.get_component("SoundComponent").play()
