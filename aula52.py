"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'Caio'
noutra_variavel = nome
nome = 'Luiz'
print(nome) # Luiz
print(noutra_variavel) # Caio


lista_a = ['Luiz', 'Caio']
lista_b = lista_a

lista_a[0] = 'Daniel' # Modifica lista B
print(lista_b) # ['Daniel', 'Caio']

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a) # ['Qualquer coisa', 'Maria', 1, True, 1.2]
print(lista_b) # ['Luiz', 'Maria', 1, True, 1.2]


