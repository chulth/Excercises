

class calculadora:

	def sumar(n1,n2):
		return n1 + n2

	def restar( n1,n2):
		return n1 - n2

	def multiplicar( n1,n2):
		return n1* n2

	def dividir (n1,n2): 
		return n1/ n2

	def exponente( n1,n2):
		return n1** n2

	def raiz( n1,n2):
		return n1 % n2

calc = calculadora.sumar(2,5)
print(calc)
calc = calculadora.restar(20,10)
print(calc)
calc = calculadora.multiplicar(3,10)
print(calc)
calc = calculadora.dividir(3,10)
print(calc)
calc = calculadora.exponente(3,10)
print(calc)
calc = calculadora.raiz(3,10)
print(calc)



