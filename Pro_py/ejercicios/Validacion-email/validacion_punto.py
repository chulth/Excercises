email = input("ingrese su email: ")
punto  = email.count(".")


if (punto < 1 or email.rfind(".") <= 1 ):
	print('el mail no contienen puntos')

else:  		
	print ('email correcto')
