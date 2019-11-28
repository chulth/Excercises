from tkinter import *

root = Tk()
root.title("salidas del aeropuerto")
#foto = iconbitmap()
#foto = PhotoImage (File = "avion.png")
#Label(root, Image=foto).pack()
def opcionesviaje():
	opcionescogida =""

	if (manana.get()==1):
		opcionescogida+=" viajaras en la mañana"

	if (tarde.get()==1):
		opcionescogida+=" viajaras en la tarde"

	if (noche.get()==1):
		opcionescogida+=" viajaras en la noche"

	textofinal.config(text= opcionescogida)

root.iconbitmap("avion.ico")
frame_1 = Frame(root)
frame_1.pack()



Label(frame_1, text ="salidas de aviones", width = 50).pack()

Checkbutton (frame_1, text= "Salidas en la mañana") #variable = manana, onvalue = 1, offvalue = 0, command= opcionesviaje).pack()

Checkbutton (frame_1, text= "Salidas en la tarde") #, variable= tarde, onvalue = 1, offvalue = 0, command= opcionesviaje).pack()

Checkbutton (frame_1, text= "Salidas nocturnas") #, variable= noche , onvalue = 1, offvalue = 0, command= opcionesviaje).pack()



textofinal= Label(frame_1)
textofinal.pack()

root.mainloop()+



"""( "UPDATE VENDEDORES SET NOMBRE = '" + Nombre.get() +
		"', APELLIDO = '" + Apellido.get() + 
		"', DIRECCION ='" + Direccion.get() +  
		"', PASSWORD ='" + Password.get() + 
		"', COMENTARIO'" + Entradacom.insert("1.0", END) +
		"' WHERE ID =" + ID_vendedor.get() )"""
		


































































