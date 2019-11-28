email  = input("escribe aqui tu email: ")

arroba = email.count('@')

if (arroba != 1 or email.rfind('@')== (len(email)-1) or email.find('@')==0):
	print("email no contiene arroba")
else:   	
	print ('contiene arroba')


