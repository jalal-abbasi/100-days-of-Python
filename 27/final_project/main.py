import tkinter


def button_clicked():
    miles = textbox.get()
    miles = float(miles)
    mile_to_km = round(miles * 1.60934,2)
    mile_to_km = str(mile_to_km)
    Label_2.config(text=mile_to_km)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=300, height=100)
window.config(padx=10, pady=20)




# textbox
textbox = tkinter.Entry(font=('Arial', 16, 'bold'))
textbox.grid(row=0, column=1)
textbox.config(width=6)




Label_1 = tkinter.Label(text="   Miles", font=('Arial', 16))
Label_1.grid(row=0, column=2)

Label_2 = tkinter.Label(text="Is equal to: ", font=('Arial', 16))
Label_2.grid(row=1, column=0)


Label_2 = tkinter.Label()
Label_2.grid(row=1, column=1)

Label_4 = tkinter.Label(text="Km", font=('Arial', 16))
Label_4.grid(row=1, column=2)

button_calculate = tkinter.Button(text="calculate", command=button_clicked)
button_calculate.grid(row=2, column=1)


window.mainloop()