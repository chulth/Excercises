from tkinter import *

raiz = Tk()
raiz.title("Factura de venta")
raiz.resizable(1,1)
#raiz.geometry("500x300") por lo general la raiz toma el tamaño del frame
raiz.iconbitmap("rick.ico")
raiz.config(bg="blue")

mainframe=Frame()
#mainframe.pack(side="left", anchor = "n") mantiene el framework en la posicion izquierda y arriba

mainframe.pack(side="top", anchor = "n" , expand = 1)

mainframe.config(width="800", height="400")
mainframe_2=Frame()
mainframe_2.pack(side="left", anchor = "n")
mainframe_2.config(width = "800" , height = "400")

#frame 3
#mainframe_3=Frame()
#mainframe_3.pack(side="bottom", anchor = "s")
#mainframe_3.config(width = "800" , height = "400")

#esta es otra forma de definir un marco absoluto
"""mainframe_2=Frame()
mainframe_2.pack(fill = "both" , expand = " TRUE")
mainframe_2.config(width = "350" , height = "400")"""

#----------------------------------------------------------
#AQUI EMPIEZA LA CONSTRUCCION DE LOS LABELS

LNumero=Label(mainframe, text="Numero")
LNumero.grid(row = 1 , column  = 1, padx = 10 , pady = 10)
TNumero=Entry(mainframe, text="Numero")
TNumero.grid(row = 1 , column  = 2, padx = 10 , pady = 10)
Cliente=Label(mainframe, text="Cliente")
Cliente.grid(row = 2 , column  = 1, padx = 10 , pady = 10)
Cliente=Entry(mainframe)
Cliente.grid(row = 2 , column  = 2, padx = 10 , pady = 10)

Ptv=Label(mainframe, text="Punto de Venta")
Ptv.grid(row = 1 , column  = 10, padx = 10 , pady = 10)
Ptv=Entry(mainframe, text="Punto de Venta")
Ptv.grid(row = 1 , column  = 11, padx = 10 , pady = 10)

Letra=Label(mainframe, text="Letra")
Letra.grid(row = 2 , column  = 5, padx = 10 , pady = 10)
Letra=Entry(mainframe, text="Letra")
Letra.grid(row = 1 , column  = 5, padx = 10 , pady = 10)

Fecha=Label(mainframe, text="Fecha")
Fecha.grid(row = 2, column  = 10, padx = 10 , pady = 10)
Fecha=Entry(mainframe, text="Fecha")
Fecha.grid(row = 2 , column  = 11, padx = 10 , pady = 10)

Total=Label(mainframe, text="Total")
Total.grid(row = 10 , column  = 10, padx = 10 , pady = 10)

Fecha=Entry(mainframe, text="Fecha")
Fecha.grid(row = 10 , column  = 11, padx = 10 , pady = 10)

"""ESTE ES UN CUADRO DE COMENTARIO CON UNA BARRA DE NAVEGACION
txtCometario=Label(mainframe, text="Cometario")
txtCometario.grid(row = 11, column  = 1, padx = 10 , pady = 10)
cuadrocomentario=Text(mainframe, width=20, height = 10)
cuadrocomentario.grid(row = 11 , column  = 2, padx = 10 , pady = 10)
scrollbar= Scrollbar(mainframe,  command=cuadrocomentario.yview)
scrollbar.grid(row = 11 , column = 3, sticky = "nsew")
cuadrocomentario.config(yscrollcommand = scrollbar.set )"""
#botonera

cmdant = Button(mainframe_2, text = "Anterior")
cmdant.grid(row = 1 , column = 5)

cmdnew = Button(mainframe_2, text = "Nuevo")
cmdnew.grid(row = 1 , column = 6)


cmdnex = Button(mainframe_2, text="Siguiente")
cmdnex.grid(row =1, column=7)

cmdmod = Button(mainframe_2, text = "Modificar")
cmdmod.grid(row = 1 , column = 8)

cmdbus=Button(mainframe_2, text="Buscar")
cmdbus.grid(row =1 , column=9)

cmdeli=Button(mainframe_2, text="Eliminar")
cmdeli.grid(row =1 , column=10)

cmdcan=Button(mainframe_2, text="Cancelar")
cmdcan.grid(row =1 , column=11)

cmdgua=Button(mainframe_2, text="Guardar")
cmdgua.grid(row =1 , column=12)

raiz.mainloop()