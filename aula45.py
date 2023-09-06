"""
Iterável -> str, range, etc (__iter__) método iter
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador (objeto)
__ = thunder
"""

texto = iter('Caio') # __iter__()
print(texto) # <str_ascii_iterator object at 0x00000216BE05EC20>

print(texto.__next__()) # C
# print(next(texto)) # C
print(texto.__next__()) # A
print(texto.__next__()) # I
print(texto.__next__()) # O

print('--------------------')

# For faz isso daqui!
text02 = 'Caio Padilha' # Iterável
iterador = iter(text02) # iterador, que é um objeto que sabe iterar minha string

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break