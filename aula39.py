# Iterando strings com while

nome = 'Caio Padilha'
indice = 0
nova_string = ''

while indice < len(nome):
    letra = nome[indice]
    nova_string += letra + '#'  # *C*a*i*o* *P*a*d*i*l*h*a
    indice += 1

print(nova_string)

    