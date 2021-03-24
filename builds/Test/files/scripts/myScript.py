from files.scripts.script import Script


class Myscript(Script):
    def __init__(self, engine):
        super().__init__(engine, "myScript")
        self.number_sprite = 0
        self.time = 15
    
    def start(self):
        spritesheet = self.game_object.get_component("SpriteSheetComponent")
        self.number_sprite = spritesheet.sprite_number[0] * spritesheet.sprite_number[1]
    
    def update(self):
        if self.time <= 0:
            spritesheet = self.game_object.get_component("SpriteSheetComponent")
            spritesheet.current_sprite += 1
            if spritesheet.current_sprite == self.number_sprite:
                spritesheet.current_sprite = 0
            spritesheet.update_render()
            self.time = 15
        self.time -= 1

