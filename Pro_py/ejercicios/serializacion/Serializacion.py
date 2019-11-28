import pickle

#este metodo open crea un fichero con los elementos de la lista de nombres

""""lista_nombres = ["Diana","John","Alejandra","Pablo", "Mercedes","Ovidio","Marina","Miguel"]

fichero_binario = open("lista_nombres","wb")

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()"""
# luego de crear el archivo con el fichero vamos a manejarlo
#abirmos el archivo
fichero = open("lista_nombres","rb")

#cargamos la informacion
lista= pickle.load(fichero)

print(lista)
