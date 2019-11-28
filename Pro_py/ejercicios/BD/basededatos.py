import sqlite3
conexiondragon = sqlite3.connect("Prudemo")
cursorp= conexiondragon.cursor()
# esta linea sirve para crear una gtabla en sql, en este caso una tabla de articulos
#cursorp.execute( "CREATE TABLE ART(CODART VARCHAR(15), DESART VARCHAR(50), CANART INTEGER(15,2), PRECUN INTEGER(15,2), ALICIVA INTEGER(5,2), MONTO INTEGER(15,2))" )

#con los siguoente comands se hace la insercion de datos masivos, hay que saber como es la estructura de la tabla que hay que insertar

ingresodedatos=[

("1010001",	"Remera Cuello Redondo Estampado Autos",	1,	500,	91,	500),
("1010001",	"Remera Cuello Redondo Estampado Autos",	1,	500,	86,	500),
("1010001",	"Remera Cuello Redondo Estampado Autos",	3,	500, 	260, 1.500),
("1010001",	"Remera Cuello Redondo Estampado Autos",	1,	500, 	86,	500),
("1010001",	"Remera Cuello Redondo Estampado Autos",	1,	500, 	86,	500),
("1010001",	"Remera Cuello Redondo Estampado Autos",	1,	500,	86,	500)

]
#EN ESTA LINEA SE INGRESARON LOS VALORES  DE LA TUPLA INGRESAR DATOS
cursorp.executemany("INSERT INTO ART VALUES(?,?,?,?,?,?)", ingresodedatos)
# EN ESTA LINEA SE HACE UN LLAMADO A LA TABLA PARA QUIE MUESTRE LOS DATOS QUE SE ENCUENTRAN EN LA TABLA

"""
cursorp.execute("SELECT * FROM ART")
datos = cursorp.fetchall()
for articulos in ingresodedatos:
	print(ariculos[0])
conexiondragon.commit()

conexiondragon.close() 