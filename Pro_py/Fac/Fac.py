import pickle 
from pickle import * 

"""class factura:

	def __init__ (self, numFac, ptv, fecFac, totalFac):
		self.numFac
		self.ptv 		= 0
		self.fecFac 	= {}
		self.letrafac 	= ""
		self.cliente 	= 0
		self.totalFac 	= 0
		self.articulo 	= ""

	def __str__():
		return "{} {} {} {} {} {} {} {}".format(self.numFac, self.ptv, self.fecFac, self.letrafac, self.cliente, self.totalFac, self.articulo)

	#def validarFactura(self, numFac, ptv, fecFac, cliente, totalFac):
		#if self.numFac > 0 """

class cliente:

	def __init__ (self, nombre, apellido, edad, genero):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.genero = genero
		print("Se ha generado un nuevo cliente con el nombre : " , self.nombre)

	def __str__(self):
		return "{} {} {} {} ".format(self.nombre, self.apellido, self.edad, self.genero)
	 	

"""esta lista contendra los clientes que estan en el sistema""" 	

class misClientes:

	lista_clientes=[]

	def __init__(self):

		listaDeClientes = open("ficheroExterno", "ab+")
		listaDeClientes.seek(0)	

		try: 
			self.lista_clientes = pickle.load(listaDeClientes)
			print("Se cargaron {} clientes en el fichero externo".format(len(self.lista_clientes)))

		except:
			print("La lista esta vacia")

		finally:
			listaDeClientes.close()

	def agregarcliente(self , persona ):
		self.lista_clientes.append(persona)
		self.guardarclientesenficheroexterno()

	def mostrarcliente(self):
		for persona in self.lista_clientes:
			print(persona)

	def guardarclientesenficheroexterno(self):
		listadeclientes=open("ficheroExterno", "wb+")
		pickle.dump(self.lista_clientes, listadeclientes)
		listadeclientes.close()

	def mostrarInfoFicheroExterno(self):
		print("se ha cargado la informacion del fichero externo")
		for persona in self.lista_clientes:
			print(persona)

miLista = misClientes()
persona = cliente( "Sandra",  "Ramirez", 28, "Femenino")
miLista.agregarcliente(persona)
persona = cliente( "Pedro",  "Bello", 50, "Masculino")
miLista.agregarcliente(persona)
persona = cliente( "Nani",  "Perez", 25, "Femenino")
miLista.agregarcliente(persona)
persona = cliente( "Alfredo",  "Justo", 36, "Masculino")
miLista.agregarcliente(persona)
persona = cliente( "Nair",  "Gonzalez", 20, "Femenino")
miLista.agregarcliente(persona)
persona = cliente( "Yairo",  "Yames", 30, "Masculino")
miLista.agregarcliente(persona)
persona = cliente( "Milena",  "Ramos", 22, "Femenino")
miLista.agregarcliente(persona)
persona = cliente( "Nicolas",  "Neron", 31, "Masculino")
miLista.agregarcliente(persona)
persona = cliente( "Liliana",  "Pinzon", 28, "Femenino")
miLista.agregarcliente(persona)

miLista.mostrarcliente()
miLista.mostrarInfoFicheroExterno()



