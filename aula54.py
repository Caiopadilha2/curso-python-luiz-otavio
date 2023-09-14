""""
Exercício
Exiba os índices da lista
0 maria
1 helena
2 luiz
"""

lista = ['Maria', 'Helena', 'Luiz']

lista.append('Caio')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])