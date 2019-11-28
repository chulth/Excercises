from tkinter import *

root = Tk()
root.title("salidas del aeropuerto")
foto = PhotoImage (file = "avion.png")
label(root, Image=foto).pack()

frame_1 = frame()
frame_1.pack()

Label(frame_1, text ="salidas de aviones", width = 50).pack()

checkbutton (frame_1, text= "Salidas nocturnas").pack()

checkbutton (frame_1, text= "Salidas en la mañana").pack()

checkbutton (frame_1, text= "Salidas en la tarde").pack()

root.mainloop()