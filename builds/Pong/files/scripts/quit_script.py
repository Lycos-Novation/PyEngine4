from files.scripts.script import Script


class Quit_Script(Script):
    def __init__(self, engine):
        super().__init__(engine, "quit_script")
    
    def click(self):
        self.engine.stop_game()
