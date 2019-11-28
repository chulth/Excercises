
#recordemos que si una variable contiene algo y de condiciona es True, por lo cual no habria que preguntarle si es verdadera la condicion
dia_de_semana = "domingo"
if dia_de_semana:
  print("Hoy se juega al futbol!!!")

#------------------ comparacion de variables con e condicional if, y el else

num = 360

if num < 180:
  print(num, 'es menor a 180')
else:
  print(num, 'no es menor a 180')

"""
En Python, estos operadores son:

    not: Niega una expresión.
    and: Evalúa potencialmente dos expresiones; si ambas son verdaderas, devuelve True, pero si alguna o ambas son falsas, devuelve False.
    or: Evalúa potencialmente dos expresiones; si alguna es verdadera, devuelve True, pero si ambas son falsas, devuelve False. 

if condicion_1:
    bloque 1
elif condicion_2:
    bloque 2
else:
    bloque 3

     este seria un bloque elif bien estructurado


"""
#ejemplo de como contruir una condicion anidada
num = 4
if num % 2 == 0:
    # dentro de este nivel se cumple que num dividido 2 no tiene resto
    if num > 0:
        # dentro de este nivel se sigue cumpliendo que num dividido 2 no tiene resto
        # pero, además, num es positivo
        print('Las dos condiciones son correctas')
    else:
        # este else corresponde al segundo if
        # dentro de este else, num no es mayor que cero.
        print(num, 'no es mayor que cero')
else:
    # este else corresponde al primer if
    # dentro de este else, num dividido 2 tiene resto
    print(num, 'dividido 2 tiene resto')

num = 10
if num > 5:
    print('a')
    if num % 2 == 0:
        print('b')
    else:
        print('c')
else:
    print('d')


 #   ¿Cuáles de estas expresiones se evalúan como True? Considerar las siguientes variables:


A = True
B = True
C = False

if A and B and C:
	print("!yaaa")

if not A or B:
	print("voyyy")


if len("Marta") == 4 or True:
	print("Aaaaa")

if A or not B and A == B:
	print(3)

palabra_1 = 'Python'

palabra_2 = 'Una frase'
#No se imprime ningún valor, ya que despúes del else no se admite una operación lógica.
if len(palabra_1) > len(palabra_2):
    print(palabra_1)

else :
    print(palabra_2)

