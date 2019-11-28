varios = [1, 'a', 2, "b", 3, "c", 4, 'd', 5, "e"]
primos  = varios[8: 1: -4]
print(primos)

sede_dh = {'barrio': 'Nunez', 'direccion': 'Monroe 860', 'lugar': 'Digital House'}
sede_dh.update ({'barrio' : 'Vila Olimpia','direccion' : 'Av. Dr. Cardoso de Melo, 90' ,  'pais' : 'Brasil' })

print(sede_dh)

verduras = ('berenjena','lechuga','tomate','coliflor','zanahoria')
print(verduras[2])

peso_bolsa_canicas = 234.0
canicas_por_bolsa = 14

peso_canica = peso_bolsa_canicas / canicas_por_bolsa
peso_cinco_canicas = round(peso_canica * 5, 2) 

print(peso_cinco_canicas)

varios = [1, 'a', 2, "b", 3, "c", 4, 'd', 5, "e"]
primos  = varios[: :]=[2,3,5]
print(primos)