from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        file = open("data.txt")
        score_in_file = file.read()
        self.highscore = int(score_in_file)
        file.close()

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()






