import sqlite3
concursor = sqlite3.connect("DBGESTOR")
cursorx= concursor.cursor()
#cursorx.execute("CREATE TABLE PRODUCT (CODIGO_ARTICULO VARCHAR (15) PRIMARY KEY,NOMBRE_ARTICULO VARCHAR (50), PRECIO INTEGER,SECCION VARCHAR(20))")

#De esta forma podemos agragar varios registros a la misma tabla
"""
Productos = [
	("Art01","vestido de mujer","550","Ropa de mujer"),
	("Art02","vestido de nena","550","Ropa niña"),
	("Art03","vestido de bebe","550","Ropa de bebe"),
	("Art04","camisa de hombre","550","Ropa de hombre"),
	("Art05","remera de mujer","550","Ropa de mujer"),
	("Art06","pantalon de hombre","550","Ropa de hombre")
]
"""
cursorx.execute("INSERT INTO PRODUCT  VALUES('art03','vestido de mujer', 500, 'Ropa de mujer')")

concursor.commit()
concursor.close()