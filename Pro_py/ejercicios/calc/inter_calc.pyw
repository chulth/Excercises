from math import *
from tkinter import *

raiz = Tk()
raiz.resizable(0,0)
#inter_caraiz.iconbitmap("calc.ico")
raiz.config(bg="blue")
raiz.title("Calculadora")
frame_1=Frame()
operacion = ""
resultado = 0
#mainframe.pack(side="left", anchor = "n") mantiene el framework en la posicion izquierda y arriba
frame_1.pack(side="top")
frame_1.config(width="400", height="400")

#----------------------------pantalla
numeroPantalla = StringVar()
pantalla = Entry(frame_1, textvariable = numeroPantalla )
pantalla.grid(row=1, column = 1 , padx=10, pady = 10)
pantalla.config(background="black", fg="#03f941", justify="right")


#----------------------------funcion teclado

def teclado(num1):
	global operacion

	if operacion != "":
		numeroPantalla.set(num1)

		operacion=""

	else:
		numeroPantalla.set(numeroPantalla.get()+num1)

#---------------------------funcion suma

def suma(num1):
	global operacion
	global resultado
	resultado+= int(num1) #resultado = resultado + num1
	operacion = "suma"
	numeroPantalla.set(resultado)

#---------------------------funcion resta

def resta(num):
	global operacion
	global resultado
	resultado-=int(num)
	operacion = "resta"
	numeroPantalla.set(resultado)

#---------------------funcion multiplicar
def multiplicar(num):
	global operacion
	global resultado
	resultado= resultado * int(num)
	operacion = "multiplicar"
	numeroPantalla.set(resultado)
#----------------------funcion division
def division(num):
	global operacion
	global resultado
	resultado/=int(num)
	operacion = "division"
	numeroPantalla.set(resultado)


#-------------------------funcion resultado
def el_resultado():
	global resultado
	numeroPantalla.set(resultado+ int(numeroPantalla.get()))
	resultado = 0

#-------------------------funcion borrar todo

def borrar():
	global resultado
	numeroPantalla.clear()

#------------------------- frame botonera

frame_2 = Frame()	
frame_2.pack(side="bottom")
frame_2.config(width="800", height="400")


#------------------------ botones

cmdnewcc = Button(frame_2, text = "CE" , command= lambda: borrar())
cmdnewcc.grid(row = 1, column = 1)

cmdnewc = Button(frame_2, text = "C" , command= lambda: borrar())
cmdnewc.grid(row = 1 , column = 2)

cmdsup = Button(frame_2, text = "<-" , command= lambda: borrar())
cmdsup.grid(row = 1, column = 3)

cmdDiv = Button(frame_2, text = "/" , command= lambda: division(numeroPantalla.get()))
cmdDiv.grid(row = 1 , column = 4)

#----------------------segunda fila

cmdnueve = Button(frame_2, text = "9" , command= lambda: teclado ("9"))
cmdnueve.grid(row = 2 , column = 3)

cmdeight = Button(frame_2, text = "8" , command= lambda: teclado ("8"))
cmdeight.grid(row = 2 , column = 2)

cmdseven = Button(frame_2, text = "7" , command= lambda: teclado ("7"))
cmdseven.grid(row = 2 , column = 1)

cmdplus = Button(frame_2, text = "+" , command= lambda: suma(numeroPantalla.get()))
cmdplus.grid(row = 2 , column = 4 )

#---------------------------tercera fila.

cmdsix = Button(frame_2, text = "6" , command= lambda: teclado ("6"))
cmdsix.grid(row = 3 , column = 3)

cmdfive = Button(frame_2, text = "5" , command= lambda: teclado ("5"))
cmdfive.grid(row = 3 , column = 2)

cmdfour = Button(frame_2, text = "4" , command= lambda: teclado ("4"))
cmdfour.grid(row = 3 , column = 1)

cmdmenos = Button(frame_2, text = "-" , command= lambda: resta(numeroPantalla.get()))
cmdmenos.grid(row = 3 , column = 4)

#----------------------------cuarta fila

cmdtre = Button(frame_2, text = "3" , command= lambda: teclado ("3"))
cmdtre.grid(row = 4 , column = 3)

cmdtwo = Button(frame_2, text = "2" , command= lambda: teclado ("2"))
cmdtwo.grid(row = 4 , column = 2)

cmdone = Button(frame_2, text = "1" , command= lambda: teclado ("1"))
cmdone.grid(row = 4 , column = 1)

cmdper = Button(frame_2, text = "*" , command= lambda: multiplicar(numeroPantalla.get()))
cmdper.grid(row = 4 , column = 4)

#-------------------------Quinta fila

cmdcero = Button(frame_2, text = "0" , command= lambda: teclado ("0"))
cmdcero.grid(row = 5 , column = 2)

cmdnewc = Button(frame_2, text = "Re" , command= lambda: el_resultado())
cmdnewc.grid(row = 5 , column = 4)


#cmdcom = Button(frame_2, text = "," , command = lambda : teclado (","))
#cmdcom.grid(row = 5, column = 1)

#cmdpun = Button(frame_2, text = "." , comand = lambda : teclado ("."))
#cmdpun.grid(row = 5 , column = 3)


raiz.mainloop()