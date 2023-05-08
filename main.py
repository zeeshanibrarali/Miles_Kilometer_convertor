from tkinter import *

window = Tk()
window.title('Mile to KM Converter')
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)


def miles_to_km():
    num = round(float(inp.get()) * 1.609)

    lab_3.config(text=f"{num}")


inp = Entry()
inp.focus()
inp.config(width=10)
inp.grid(column=1, row=0)

lab = Label()
lab.config(text='is equal to', padx=20, font=('Arial', 20, 'normal'))
lab.grid(column=0, row=1)
lab_1 = Label()
lab_1.config(text='Miles', padx=20, font=('Arial', 20, 'normal'))
lab_1.grid(column=3, row=0)
lab_2 = Label()
lab_2.config(text='Km', padx=20, font=('Arial', 20, 'normal'))
lab_2.grid(column=3, row=1)

lab_3 = Label()
lab_3.config(text='0', padx=20, font=('Arial', 20, 'normal'))
lab_3.grid(column=1, row=1)

butt = Button(text='Calculate', command=miles_to_km)
butt.grid(column=1, row=2)


window.mainloop()

