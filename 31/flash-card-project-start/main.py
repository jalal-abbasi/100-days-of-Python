from tkinter import *

import pandas
from pandas import read_csv
import random

BACKGROUND_COLOR = "#B1DDC6"

# Data_Frame
try:
    data_frame = read_csv('data/words_to_learn.csv')
except:
    data_frame = read_csv('data/french_words.csv')

to_learn = data_frame.to_dict(orient="records")


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("FlashCard")
random_item = {}


def generate_next_card():
    global random_item
    global card_wait_time
    window.after_cancel(card_wait_time)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(language_name, fill="black", text="French")
    random_item = random.choice(to_learn)
    canvas.itemconfig(word, fill="Black", text=random_item["French"])
    # card_wait_time = window.after(3000, show_the_answer)
    card_wait_time = window.after(3000, show_the_answer)


def remove_the_correct_answer():
    to_learn.remove(random_item)
    generate_next_card()
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv('data/words_to_learn.csv', index=False)



def show_the_answer():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language_name, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=random_item["English"])


# Canvas
canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
language_name = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 253, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)



# Buttons
button_right_image = PhotoImage(file="./images/right.png")
button_right = Button(image=button_right_image, highlightthickness=0, command=remove_the_correct_answer)
button_right.grid(row=1, column=1)

button_wrong_image = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=button_wrong_image, highlightthickness=0, command=generate_next_card)
button_wrong.grid(row=1, column=0)

card_wait_time = window.after(3000, show_the_answer)
generate_next_card()

window.mainloop()
dict(to_learn)


