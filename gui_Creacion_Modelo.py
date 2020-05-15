from tkinter import *
from PIL import ImageTk, Image

car_name = Tk()
car_name.title("Nuevo modelo")

choose_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Guillermo\\Desktop\\Machinery\\logo.png"))

texto1 = Label(car_name, text= "Asignando nuevo modelo a la flota")
texto1.grid(row = 0, column = 0)

texto2 = Label(car_name, text= "Indica aquí el nombre del modelo:")
texto2.grid(row = 1, column = 0)


entrada_nombre = Entry(car_name, bd = 5, width = 60)
entrada_nombre.grid(row = 2, column = 0)

def GetNombre():
    global nombre_modelo
    nombre_modelo = entrada_nombre.get()
    last = len(nombre_modelo)
    entrada_nombre.delete(0, last)
    return

boton_texto = Button(car_name,text="Aceptar", command = GetNombre)
boton_texto.grid(row=3, column = 0)

imagen = Label(image = choose_img)
imagen.grid(row=4, column = 0)


car_name.mainloop()
