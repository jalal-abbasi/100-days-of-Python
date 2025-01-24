import time
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title("Quizler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)
        self.quiz = quiz
        self.question_text = self.quiz.next_question()

        # Canvas
        self.canvas = Canvas(bg="white", height=250, width=300, highlightthickness=0)  # no need to feed the root widget
        # we get the output of create_text inside a new variable: the output is the widget id, so to change it later
        self.canvas_text = self.canvas.create_text(
            150, 125,
            width=220,
            fill="black",
            font=("Arial", 15, "italic"),
            text=self.question_text)
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        # True and False Buttons
        true_image = PhotoImage(file=r"images\true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.click_true_button)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file=r"images\false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.click_false_button)
        self.false_button.grid(row=2, column=1)

        # Label
        self.label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.window.mainloop()

    def click_true_button(self):
        self.give_feedback_and_delay(self.quiz.check_answer("True"))

    def click_false_button(self):
        self.give_feedback_and_delay(self.quiz.check_answer("False"))

    def give_feedback_and_delay(self, is_correct):
        if is_correct:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(500, self.generate_next_question)

    def generate_next_question(self):
        self.canvas.configure(bg="white")
        self.label.configure(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"The Fucking Game is Over! "
                                                          f"\nYour score is {self.quiz.score}/10")
            self.true_button.configure(state="disabled")
            self.false_button.configure(state="disabled")




