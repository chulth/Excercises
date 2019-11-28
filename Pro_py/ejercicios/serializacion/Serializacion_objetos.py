import pickle	

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
#creo los objetos que quiero manipular
coche_1 =  vehiculo( "Mazda", "Mr5")
coche_2 =  vehiculo( "Toyota", "Jr5")
coche_3 =  vehiculo( "Mercedes", "X6")
coche_4 =  vehiculo( "Renault", "V4")

#creo la coleccion de autos 
misAutos = [coche_1,coche_2, coche_3, coche_4]
#creo el archivo donde voy a cargar la info
ficheroautos = open("Miscoches","wb")
#cargo la informacion de mis autos en mi fichero auto
pickle.dump(misAutos, ficheroautos)

ficheroautos.close()


