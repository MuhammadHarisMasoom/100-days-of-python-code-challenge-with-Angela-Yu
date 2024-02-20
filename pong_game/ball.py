from turtle import Turtle, Screen

# class Ball:
#     def __init__(self):
#         self.ball = Turtle()
#         self.ball.color("white")
#         self.ball.shape("circle")
#         # Get screen size
#         self.screen = Screen()
#         self.screen_width = self.screen.window_width()
#         self.screen_height = self.screen.window_height()
#
#         # Calculate coordinates for the top-right corner
#         self.top_right_x = self.screen_width / 2
#         self.top_right_y = self.screen_height / 2
#
#         # Move turtle to the top-right corner
#         self.ball.penup()
#         self.ball.goto(self.top_right_x, self.top_right_y)
#         self.ball.pendown()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
