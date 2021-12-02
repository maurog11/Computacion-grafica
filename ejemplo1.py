from tkinter import *
from tkinter import messagebox

def CheckOpcion():
    MiTexto = "Casilla 1= " + str(op1.get())+"\n Casilla 2= " + str(op2.get()) + "\n Casilla 3= " + str(op3.get())
    print(MiTexto)
    messagebox.showinfo('Casillas de verificacion',MiTexto)

MiVentana = Tk()
MiVentana.geometry('640x480')
MiVentana.title("Ejemplo de controles en Tkinter")
lbNum1 = Label(MiVentana, text="Ejemplo de checkbox",font=("Arial Bold",10))
op1 = IntVar()
op2 = IntVar()
op3 = IntVar()
CheckOpcion1 = Checkbutton(MiVentana,text='Casilla 1',variable=op1,width=10)
CheckOpcion2 = Checkbutton(MiVentana,text='Casilla 2',variable=op2,width=10)
CheckOpcion3 = Checkbutton(MiVentana,text='Casilla 3',variable=op3,width=10)
btEvaluar = Button(MiVentana,text="Evaluar",command=CheckOpcion)
lbNum1.grid(column=0,row=0)
CheckOpcion1.grid(column=0,row=2)
CheckOpcion2.grid(column=1,row=2)
CheckOpcion3.grid(column=2,row=2)
btEvaluar.grid(column=2,row=3)

MiVentana.mainloop()
