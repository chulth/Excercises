import pickle
#abro mi fichero
ficherodeApertura=open("Miscoches", "rb")

#cargo la info que tiene el archivo

loscoches = pickle.load(ficherodeApertura)

ficherodeApertura.close()

for c in loscoches:
	print(c.modelo())

