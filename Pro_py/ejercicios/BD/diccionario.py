# Se definen los elementos del diccionario como pares clave:valor
mi_dict = {'clave_1': 123, 'clave_2': 100, 'clave_3': 311}

# Se accede a un valor particular a través de su clave
print(mi_dict['clave_2'])
#la sintaxis de un diccionario comprensivo seria :
#{**expresión_para_clave** : **expresión_para_valor** for **elemento** in **iterable** [if **condición**]}
animales = ['ballena', 'elefante', 'gallina']

mi_diccionario = {x:len(x) for x in animales}
print(mi_diccionario)