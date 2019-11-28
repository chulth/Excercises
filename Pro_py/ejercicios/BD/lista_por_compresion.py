# Definimos una lista
enteros = [1, 2, 3, 4, 5]

# Definimos una lista por comprensión
enteros_mas_uno = [numero + 1 for numero in enteros]

print(enteros_mas_uno)

#en un listado por comprension podemos sumar dos variable e iterarlas en un ciclo for, en una linea
#esta es la sintaxis de un comando de lista por comprension con ciclo for
#[**expresión** for **elemento** in **iterable**]

# definimos una lista
enteros = [1, 2, 3, 4, 5]

# definimos una lista por comprensión en la cual estamos agrgando un condicional if, para filtrar la operacion
#[**expresión** for **elemento** in **iterable** [if **condición]]

enteros_mas_uno = [numero + 1  for  numero  in  enteros if numero > 3]

print(enteros_mas_uno)
#---------------------------------------- ejercicios


