from turtle import * 
shape("turtle")
speed(8)
pensize(5)
pencolor("green")
Windows = Screen()
tortuga = Turtle()

lados = 4
distancia = 1800
giro = 90

for count in range(lados):
	forward(distancia)
	left(giro)


#esta es una forma sencilla de hacer un cuadrado pero para hacerla mas logica se cambian con variables
"""for count in range (5):
	forward(100)
	left(90)"""

"""este codigo recorre i hasta llegar a 1800 de 10 en 10 y como tiene un left de 3 cada 10 gira 3 grados con lo cual hace un circulo
i = 0
while i <= 1800:
 	tortuga.left(3)
 	tortuga.forward(10)
 	i += 10 """



window.mainloop()