class Scene:
    def __init__(self, name, color, game_objects):
        self.name = name
        self.bg_color = color
        self.__game_object_count = 0
        self.game_objects = []
        self.add_game_objects(game_objects)

    def add_game_objects(self, game_objects):
        for i in game_objects:
            self.add_game_object(i)

    def add_game_object(self, entity):
        self.game_objects.append(entity)
        entity.id_ = self.__game_object_count
        self.__game_object_count += 1

    def get_game_object(self, id_):
        for i in self.game_objects:
            if i.id_ == id_:
                return i

    def start(self):
        for i in self.game_objects:
            i.start()

    def key_press(self, evt):
        for i in self.game_objects:
            i.key_press(evt)

    def key_release(self, evt):
        for i in self.game_objects:
            i.key_release(evt)

    def mouse_press(self, evt):
        for i in self.game_objects:
            i.mouse_press(evt)

    def mouse_release(self, evt):
        for i in self.game_objects:
            i.mouse_release(evt)

    def mouse_motion(self, evt):
        for i in self.game_objects:
            i.mouse_motion(evt)

    def mouse_wheel(self, evt):
        for i in self.game_objects:
            i.mouse_wheel(evt)
    
    def update(self):
        for i in self.game_objects:
            i.update()

    def show(self, screen):
        screen.fill(self.bg_color)

        for i in self.game_objects:
            i.show(screen)
