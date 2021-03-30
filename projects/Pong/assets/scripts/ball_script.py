from files.scripts.script import Script


class Ball_Script(Script):
    def __init__(self, engine):
        super().__init__(engine, "ball_script")
        self.time = 0
    
    def update(self, deltatime):
        transform = self.game_object.get_component("TransformComponent")
        auto = self.game_object.get_component("AutoComponent")

        if self.time > 0.75:
            auto.move[1] *= 1.05
            auto.move[0] *= 1.05
            self.time = 0
        self.time += deltatime

        if transform.position[1] < 0 or transform.position[1] > 710:
            auto.move[1] = -auto.move[1]
        if transform.position[0] < 0:
            score = self.engine.get_game_object(2)
            text = score.get_component("TextComponent")
            scores = text.text.split(" - ")
            text.text = scores[0] + " - P2 : " + str(int(scores[1].split(" ")[-1])+1)
            self.update_score(text, transform, auto, int(scores[1].split(" ")[-1])+1)
        if transform.position[0] > 1070:
            score = self.engine.get_game_object(2)
            text = score.get_component("TextComponent")
            scores = text.text.split(" - ")
            text.text = "P1 : " + str(int(scores[0].split(" ")[-1])+1) + " - " + scores[1]
            self.update_score(text, transform, auto, int(scores[0].split(" ")[-1])+1)
        
    def update_score(self, text, transform, auto, new_score):
        text.update_render()
        transform.position = [530, 350]
        if new_score == 5:
            text.text += "     ENDED"
            text.update_render()
            auto.move = [0, 0]
        else:
            auto.move[0] = -auto.move[0]

    def collide(self, game_object, cause):
        if game_object.id_ == 0 or game_object.id_ == 1:
            auto = self.game_object.get_component("AutoComponent")
            auto.move[0] = -auto.move[0]
