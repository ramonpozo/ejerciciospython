"""def cualSeAcercaMas (numeroSelec, numeros):
	marcador = 0

	for num in numeros:
		if (abs(numeroSelec - num) < abs(numeroSelec - marcador)):
			marcador = num

	return marcador

numeroSelec = 9
numeros = [10, 15, 9, 7]

print(cualSeAcercaMas(numeroSelec, numeros))"""

def cualSeAcercaMas (numeros):
	marcador = 0

	for num in numeros[1:]:
		if (abs(numeros[0] - num) < abs(numeros[0] - marcador)):
			marcador = num

	return marcador

numeros = [18, 14, 9, 7, 34, 21, 2, 5]

print(cualSeAcercaMas(numeros))