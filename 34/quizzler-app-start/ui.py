from tkinter import *
THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(self.window, bg="white", height=250, width=300)
        self.canvas.create_text(150, 125, fill="black", font=("Arial", 20, "italic"), text="hi")
        self.canvas.grid(column=0, columnspan=2, row=1, pady=20)

        true_image = PhotoImage(file=r"images\true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file=r"images\false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.window.mainloop()
