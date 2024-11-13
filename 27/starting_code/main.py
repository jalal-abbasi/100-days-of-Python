import tkinter

window = tkinter.Tk()

window.title("Jalal is excellent")
window.minsize(width=400, height=500)

label = tkinter.Label(text="Jalal is the best", font=("Arial", 24, "bold"))
label.pack()


def my_event():
    print("my button is clicked")
    print(my_textbox.get())

my_button = tkinter.Button(text="my button", command=my_event)
my_button.pack()

my_textbox = tkinter.Entry(width=10)
print(my_textbox.get())
my_textbox.pack()

entered_value = my_textbox.get()
window.mainloop()
