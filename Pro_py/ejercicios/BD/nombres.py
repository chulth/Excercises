import math 

nombres = ('Demian', 'Pablo', 'Paolo', 'Julian')

profesores_dh = [nombres]

for nombre in nombres:
    print(nombre)
#multiplicar una cadena por un explonente y guardarla en otra cadena
lista = [2, 4, 2, 5, 8, 1, 3]

cuadrados = []

for i in lista:
	cuadrados.append(i**2)
	print(cuadrados)

# agregar un string a cuna cadena de nombres
nombres = ['Demian', 'Pablo', 'Paolo', 'Julian']

saludos = []
x = "Hola,"
y = "!"
for i in nombres:
  saludos.append(x+ i + y)

print(saludos)

#contadores dentro de un for
contador = 0

for i in [1, 2, 3, 4, 5, 6]:
    contador = contador + 1

print(contador)

lista = [2, 5, 4, 8, 9, 3, 5 , 6]

contador = 0

for n in lista:
  contador += 1
  
print(contador)


#buscar el promedio en una lista

lista = [2, 5, 4, 8, 9, 3, 5, 6]

contador =0
sumatoria =0
media = 0

for n in lista:
  contador += 1
for x in lista:
  sumatoria +=x

media=sumatoria/ contador

print(media)