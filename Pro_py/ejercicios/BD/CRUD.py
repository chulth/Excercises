from tkinter import *
from tkinter import messagebox
import sqlite3

#----------------creacion de funciones


def conexion():
	try : 
		conexiondb = sqlite3.connect("EmpresaX")
		cursorTienda= conexiondb.cursor()
		cursorTienda.execute( '''
			CREATE TABLE VENDEDORES (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50),
			APELLIDO VARCHAR(50),
			DIRECCION VARCHAR(100),
			PASSWORD VARCHAR(15),
			COMENTARIO VARCHAR(150))''' )

		messagebox.showinfo("BBDD", "BBDD creada con exito")

	except:
		messagebox.showwarning("BBDD", "La base de datos ya existe")

def borrar():
	ID_vendedor.set("")
	Nombre.set("")
	Apellido.set("")
	Direccion.set("")
	Password.set("")
	Entradacom.delete(1.0,END)

def Cerrar(): 
	valor= messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
	if valor == "yes":
		root.destroy()

def Update(): 
	try : 
		conexiondb = sqlite3.connect("EmpresaX")
		cursorTienda = conexiondb.cursor()
		#Datos = Nombre.get(), Apellido.get() , Direccion.get() , Password.get() ,  Entradacom.get("1.0", END)

		cursorTienda.execute("UPDATE VENDEDORES SET NOMBRE= '"+ Nombre.get() +
			"' , APELLIDO ='" + Apellido.get() +
			"', DIRECCION = '" + Direccion.get() +
			"', PASSWORD='" + Password.get() +
			"', COMENTARIO ='" + Entradacom.get("1.0",END) +
			"' WHERE ID =" + ID_vendedor.get())

		#cursorTienda.execute("UPDATE VENDEDORES SET NOMBRE= ?, APELLIDO =?, DIRECCION = ? , PASSWORD =?, COMENTARIO=?" + "WHERE ID =" ID_vendedor.get(), (Datos))
		conexiondb.commit()
		messagebox.showinfo("BBDD", "BBDD ha actualizado un vendedor con exito")

	except:
		messagebox.showwarning("BBDD", "el vendedor no ha sido actualizado")


def Read(): 
	try : 
		conexiondb = sqlite3.connect("EmpresaX")
		cursorTienda= conexiondb.cursor()
		cursorTienda.execute( "SELECT * FROM  VENDEDORES WHERE ID =" + ID_vendedor.get() )
		elvendedor = cursorTienda.fetchall()
		for vendedor in elvendedor:
			ID_vendedor.set(vendedor[0])
			Nombre.set(vendedor[1])
			Apellido.set(vendedor[2])
			Direccion.set(vendedor[3])
			Password.set(vendedor[4])
			Entradacom.insert(1.0,vendedor[5])
		conexiondb.commit()
		messagebox.showinfo("BBDD", "BBDD ha encontrado al vendedor")

	except:
		messagebox.showwarning("BBDD", "el vendedor no  ya existe")

def Create():
	try : 
		conexiondb = sqlite3.connect("EmpresaX")
		cursorTienda= conexiondb.cursor()
		Datos = Nombre.get(), Apellido.get() , Direccion.get() , Password.get() ,  Entradacom.get("1.0", END)
		
		'''cursorTienda.execute( "INSERT INTO VENDEDORES VALUES ( NULL,'" + Nombre.get() +
			"','" + Apellido.get() + 
			"','" + Direccion.get() +  
			"','" + Password.get() + 
			"','" + Entradacom.get("1.0", END) + "')" )'''# esta es una forma de ingresar datos, pero no parametrizados


		cursorTienda.execute( "INSERT INTO VENDEDORES VALUES ( NULL,?,?,?,?,?)",(Datos))	
		conexiondb.commit()
		messagebox.showinfo("BBDD", "BBDD ha creado un vendedor con exito")

	except:
		messagebox.showwarning("BBDD", "el vendedor  ya existe")


def Delete(): 
	try : 
		conexiondb = sqlite3.connect("EmpresaX")
		cursorTienda= conexiondb.cursor()
		cursorTienda.execute( "DELETE FROM  VENDEDORES WHERE ID =" + ID_vendedor.get() )
		conexiondb.commit()
		messagebox.showinfo("BBDD", "Se ha borrado al vendedor")

	except:
		messagebox.showwarning("BBDD", "El vendedor no  ya existe")


#--------------------------creacion del root
root = Tk()
root.resizable(0,0)
root.title("Formulario de vendedores")
root.iconbitmap("pineapple.ico")
menubarra = Menu(root)
root.config(menu = menubarra, width = 300, height= 500)

#----------------------------creacion del menu

barraBBDD = Menu(menubarra)
barraCRUD = Menu(menubarra)
barraVer = Menu(menubarra)
barraAyuda = Menu(menubarra)

menubarra.add_cascade(label = "BBDD", menu= barraBBDD  )
menubarra.add_cascade(label = "CRUD", menu=barraCRUD  )
menubarra.add_cascade(label = "Ver", menu=barraVer  )
menubarra.add_cascade(label = "Ayuda", menu=barraAyuda  )


#barraBBDD = menu(menubarra, tearoff=0)
barraBBDD.add_command(label="Conectar", command= conexion)
barraBBDD.add_separator()
barraBBDD.add_command(label="Borrar", command= borrar)
barraBBDD.add_command(label="Cerrar", command= Cerrar)

#-----------------menu CRUD

#barraCRUD = Menu(menubarra, tearoff = 0 )
barraCRUD.add_command(label="Create", command= Create)
barraCRUD.add_command(label="Update", command= Update)
barraCRUD.add_command(label="Read", command= Read)
barraCRUD.add_command(label="Deleate",command= Delete)

#---------------------------Creacion del frame
aframe = Frame()
aframe.pack(side="top")
aframe.config(width="300", height="500")

#----------------------------id
ID_vendedor = StringVar()
labelid = Label(aframe, text="ID")
labelid.grid(row = 1, column = 1)
Entradaid = Entry(aframe, textvariable = ID_vendedor )
Entradaid.grid(row=1, column = 2 , padx= 5, pady = 5)
Entradaid.config(background="white", fg="#000", justify="right")

#---------------------Nombre
Nombre = StringVar()
labelid = Label(aframe, text="Nombre")
labelid.grid(row = 2, column = 1)
Entradanom = Entry(aframe, textvariable = Nombre )
Entradanom.grid(row=2, column = 2 , padx= 5 , pady = 5)
Entradanom.config(background="white", fg="#000", justify="right")

#---------------------Apellido
Apellido = StringVar()
labelid = Label(aframe, text="Apellido")
labelid.grid(row = 3, column = 1)
Entradaap = Entry(aframe, textvariable = Apellido )
Entradaap.grid(row=3, column = 2 , padx=5 , pady = 5)
Entradaap.config(background="white", fg="#000", justify="right")

#--------------------- Direccion
Direccion = StringVar()
labelid = Label(aframe, text="Direccion")
labelid.grid(row = 3, column = 1)
Entradadi = Entry(aframe, textvariable = Direccion )
Entradadi.grid(row=3, column = 2 , padx=5, pady = 5)
Entradadi.config(background="white", fg="#000", justify="right")

#---------------------Password
Password = StringVar()
labelid = Label(aframe, text="Password")
labelid.grid(row = 4, column = 1)
Entradapass = Entry(aframe, textvariable = Password )
Entradapass.grid(row=4, column = 2 , padx=5, pady =5)
Entradapass.config(background="white", fg="#000", justify="right")

#---------------------comentario
#comentario = StringVar()
labelid = Label(aframe, text="comentario")
labelid.grid(row = 5, column = 1)
Entradacom = Text(aframe, width="20", height="10")
Entradacom.grid(row=5, column = 2)
scrolcom=Scrollbar(aframe, command = Entradacom.yview)
scrolcom.grid(row=5, column=3, sticky = "nsew")
Entradacom.config(yscrollcommand=scrolcom.set)


#-----------------------------botonera

bframe = Frame()
bframe.pack(side="bottom")
bframe.config(width="200", height="100")
cmdnew = Button(bframe, text = "Create" , command= lambda: Create())
cmdnew.grid(row = 10, column = 1 , padx=5, pady = 5)

cmdup = Button(bframe, text = "Update" , command= lambda: Update())
cmdup.grid(row = 10, column = 2,  padx=5, pady = 5)

cmdre = Button(bframe, text = "Read" , command= lambda: Read())
cmdre.grid(row = 10, column = 3,  padx=5, pady = 5)

cmddel = Button(bframe, text = "Delete" , command= lambda: Delete())
cmddel.grid(row = 10, column = 4,  padx=5, pady = 5)




root.mainloop()
