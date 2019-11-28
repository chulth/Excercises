def mitad(num):
  	case_1: num  == float
  	division = float(num/2)
  	case_2: num == -num
  	division = -num/2
  	case_3: num ==num
  	division = num/2
  	return division


print(mitad(11))

def mitad_2(num):
	if num == float:
		division = float(num/2)
	elif num== -num:
		division = -num/mitad_2
	else :
		division = num/2
	return division 

print(mitad_2(21))

def multi(num1,num2):
	reslutado = num1*num2
	return reslutado

print(multi(-1.5,2))

def comparar_tipo(mi_objeto, tipo):
	if isinstance(mi_objeto, tipo):
		print(mi_objeto, 'es del tipo', tipo)
		return True
	else:
		print(mi_objeto, 'no es del tipo', tipo)
		return False

comparar_tipo("caballo", str)

# funcion comprobar el tipo de dato
def tipo_de_dato(dato):
	if isinstance(dato , str):
		print(True)
	elif  isinstance(dato, float):
		print(True)
	elif isinstance(dato, int):
		print(False)
	elif isinstance(dato, bool):
		print(False)
	else :
		print("no es nada")

tipo_de_dato(False)

#funcion elevar un numero
def elevado(num): # 1
    # Definimos una lista vacía
    mi_lista = [] # 2

    # Iteramos en un rango de 10 asignando un valor creciente a i (crece de 1 en 1)
    for i in range(10): # 3
        # Elevamos a la potencia dada en i y lo guardamos en num_elevado
        num_elevado = num ** i # 4
        # Guardamos al final de la lista el numero elevado a la potencia i
        mi_lista.append(num_elevado) # 5

    return mi_lista # 6

# Hacemos el llamado a la función y lo imprimimos
print(elevado(2))# 7

#funcion que comprueba si es par o impar

def lista_par_impar(lis_num):
  pares=[]
  impares=[]
  enteros= (pares, impares)
  control = 0
  for i in lis_num:
  	if (i%2 == control):
  		pares.append(i)
  	else :
  		impares.append(i)
  return  print(enteros) 

lista_par_impar((10,20,21,31,17,5,4,2,221, 1))

#utilizar funciones dentro de otras funciones
def contador(lista):
  conta=0
  for i in lista:
    conta+=1
  return conta

def sumatoria(lista):
  suma = 0
  for i in lista:
    suma+=i
  return suma
def media (lista):
  lamedia=sumatoria(lista)/contador(lista)
  return lamedia



lista=[10,100,20,3,5,50,4,5,6]
print(media(lista))
