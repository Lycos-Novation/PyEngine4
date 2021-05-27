class Scene:
    def __init__(self, engine, name, color, timescale, camera_position, camera_follow, game_objects):
        self.engine = engine
        self.name = name
        self.bg_color = color
        self.timescale = timescale
        self.camera_position = camera_position
        self.camera_follow = camera_follow
        self.__game_object_count = 0
        self.game_objects = []
        self.add_game_objects(game_objects)

    def add_game_objects(self, game_objects):
        for i in game_objects:
            self.add_game_object(i)

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)
        game_object.id_ = self.__game_object_count
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
    
    def update(self, deltatime):
        deltatime *= self.timescale

        if self.camera_follow is not None:
            if self.camera_follow is not None and self.camera_follow.get_component("TransformComponent") is not None:
                self.camera_position = self.camera_follow.get_component("TransformComponent").position - \
                                       self.engine.get_game_size() / 2

        for i in self.game_objects:
            i.update(deltatime)

    def show(self, screen):
        screen.fill(self.bg_color.rgba())

        for i in sorted(self.game_objects, key=lambda x: x.zindex):
            i.show(screen, self.camera_position)
