opcionSi = ["SI", "si", "Si", "S", "s", "Sí", "sí"]
opcionNo = ["NO", "no", "No", "N", "n"]

valido = True

while valido:
	opcion = input()

	if opcion in opcionSi:
		valido = False
		respuesta = True

	if opcion in opcionNo:
		valido = False
		respuesta = False

if respuesta:
	print("Has elegido SI")
else:
	print("Has elegido NO")