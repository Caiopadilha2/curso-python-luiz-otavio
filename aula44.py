"""
For + range
range -> range(start, stop, step)
"""

numeros = range(0, 10, 2)
# print(numeros)
# print(numeros[4])

numeros_2 = range(5, 10)
# print(numeros_2)


for numero in numeros:
    print(numero)

multiplos_de_8_0_a_100 = range(0, 100, 8)
for numero in multiplos_de_8_0_a_100:
    print(f'Múltiplos de 08 de 0 a 100, {numero}')
    