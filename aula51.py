lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)

print(lista_c)
print(lista_d) # None -> Extend não retorna nada
print(lista_a) # [1, 2, 3, 4, 5, 6]