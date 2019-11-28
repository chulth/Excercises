import sqlite3

class form:


	def cAbrir(): 
	conexiondb = sqlite3.connect("EmpresaX")
	cursorTienda= conexiondb.cursor()
	cursorTienda.execute( "CREATE TABLE VENDEDORES(ID INTEGER AUTOIMCREMENT PRIMARY KEY, NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), DIRECCION VARCHAR(100), PASSWORD VARCHAR(15), COMENTARIO VARCHAR(150)" )
	print("se aha creado la conexion")

	def Nuevo():
	conexiondb = sqlite3.connect("EmpresaX")
	cursorTienda= conexiondb.cursor()
	cursorTienda.execute("INSERT INTO VENDEDORES VALUES (ID,NOMBRE,APELLIDO,DIRECCION,PASSWORD,COMENTARIO)")
	print("Se ha guardado el registro")
		

	def Cerrar(): 
		cursorTienda.close()
		print("la conexion esta cerrada")

	def Salir(): 
		quit
	def Create():
		pass
	def Update(): 
		pass
	def Read(): 
		pass
	def Deleate(): 
		pass

