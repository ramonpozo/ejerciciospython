def sumatoria (num1, num2):
	resultado = 0;

	while num1 <= num2:
		resultado += num1
		num1 += 1

	return resultado

print(sumatoria(2, 4))