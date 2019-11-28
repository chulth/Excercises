#este metodo lo que hace es ingresar una linea de texto  con la funcion writeline[2]
from io import *
archivo_2 = open("archivo_2.txt", "r+")
txt = "Todos los dias estamos en constante lucha \n es por ello que debemos ser fuerte de alma, cuerpo y mente\n es todo lo que hay que saber"
#archivo_2.write(txt)
lista_texto = archivo_2.readlines();
lista_texto [2] = "Esta linea se ingreso desde el interior \n" 
archivo_2.seek(0)
archivo_2.writelines(lista_texto)
archivo_2.close()
