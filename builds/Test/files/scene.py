class Scene:
    def __init__(self, name, color, entities):
        self.name = name
        self.bg_color = color
        self.entities = entities
    
    def update(self):
        for i in self.entities:
            i.update()

    def show(self, screen):
        screen.fill(self.bg_color)

        for i in self.entities:
            i.show(screen)