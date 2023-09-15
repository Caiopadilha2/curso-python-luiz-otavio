""" Enumerate"""

lista = ['Maria', 'José', 'Caio']

lista_enumerada = enumerate(lista)
lista_enumerada = list(enumerate(lista)) 
print(lista_enumerada)
# print(next(lista_enumerada)) #(0, 'Maria')

for item in lista_enumerada: #é como chamar o next acima
    print(item)



nomes = ['Daniel', 'Mariana', 'Cássio']


# for item in enumerate(nomes): 
for indice, nome in enumerate(nomes):
    # indice, nome = item
    print(indice, nome)
