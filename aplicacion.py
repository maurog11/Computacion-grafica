from tkinter import *

def HacerClick():
    num1 = float(txt1.get())
    num2 = float(txt2.get())
    suma = num1+num2
    lbresultado.configure(text=suma)

window = Tk()
window.title("Aplicacion")
window.geometry('640x480')
lbl1 = Label(window, text="Numero 1",font=("Arial Bold", 10))
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="Numero 2",font=("Arial Bold", 10))
lbl2.grid(column=0, row=1)
lbresultado = Label(window, text="0",font=("Arial Bold", 10))
lbresultado.grid(column=1, row=2)
btn = Button(window, text="Suma", font=("Arial Bold", 10), bg="orange", fg="red", command=HacerClick)
btn.grid(column=1, row=3)
txt1 = Entry(window,width=10)
txt1.grid(column=1, row=0)
txt2 = Entry(window,width=10)
txt2.grid(column=1, row=1)


window.mainloop()