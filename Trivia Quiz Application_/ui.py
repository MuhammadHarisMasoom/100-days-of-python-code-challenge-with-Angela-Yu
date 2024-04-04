from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas Creation
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=5)

        # Score Label
        self.score = Label(text="Score: 0", fg="white", font=("Arial", 12), bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        # Buttons

        # Correct Button

        correct_image = PhotoImage(file='images/true.png')
        self.correct_button = Button(image=correct_image, command=self.correct_button_clicked, highlightthickness=0)
        self.correct_button.grid(row=2, column=0)

        # Incorrect Button

        incorrect_image = PhotoImage(file='images/false.png')
        self.incorrect_button = Button(image=incorrect_image, command=self.incorrect_button_clicked, highlightthickness=0)
        self.incorrect_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of quiz.")
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")
    def correct_button_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def incorrect_button_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

