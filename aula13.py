nome = 'Caio Padilha'
altura = 1.93
peso = 82
imc = peso / (altura ** 2)
# Caio tem 1.93 de altura, pesa 82kg e seu IMC é X.
print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é', imc )


#Introdução f Strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu ICM é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

