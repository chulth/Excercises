import pickle
#from serializacion.Serializacion_objetos import*

class vehiculo ():

	def __init__(self, marca, modelo):
		self.marca 		= marca
		self.modelo 	= modelo
		self.enmarcha 	= False
		self.acelera 	= False
		self.frena 		= False

	def arancar(self):
		self.enmarcha = True

	def acelerar(self):
		self.acelera = True

	def frenado(self):
		self.frena = True 

	def estado(self,):
		print( "Marca : ", self.marca ," \n Modelo: " , self.modelo, "\nEn marcha : ", self.enmarcha ,"\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)

#este metodo open crea un fichero con los elementos de la lista de nombres

""""lista_nombres = ["Diana","John","Alejandra","Pablo", "Mercedes","Ovidio","Marina","Miguel"]

fichero_binario = open("lista_nombres","wb")

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()"""
# luego de crear el archivo con el fichero vamos a manejarlo
#abirmos el archivo
fichero = open("Miscoches","rb")

#cargamos la informacion
lista= pickle.load(fichero)

for c in lista :
	print(c.estado())
