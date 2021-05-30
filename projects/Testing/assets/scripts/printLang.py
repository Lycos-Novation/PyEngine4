from files.scripts.script import Script


class Printlang(Script):
    def __init__(self, engine):
        super().__init__(engine, "printLang")
    
    def clicked(self):
        print(self.engine.lang_manager.get_langs())
        print(self.engine.lang_manager.get_translate("bonjour", "NOOOO"))
