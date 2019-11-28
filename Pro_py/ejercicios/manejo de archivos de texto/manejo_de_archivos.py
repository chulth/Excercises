from io import *

#esta es el primer metodo para crear, manipular y escrbir en un archivo
#archivo_txt = open("archivo_txt" , "w") 

frase = "Los jueves son el mejor dia para estudiar Python \n  no los miercoles"

#archivo_txt.write(frase) 


#este metodo lee el archivo anterior y los imprime por pantalla
#archivo_txt = open("archivo_txt", "r")

#texto = archivo_txt.read()

#print(texto)



#este metodo lee el archivo por lineas y genera una lista que puedo consultar

#lineas_txt = archivo_txt.readlines()

#archivo_txt.close() 


#print(lineas_txt)

#este metodo agrega una linea al archivo 
archivo_txt = open("archivo_txt", "a")
archivo_txt.write("\n siempre es mas facil aprender con comida")
archivo_txt.close()


archivo_txt = open("archivo_txt", "r")