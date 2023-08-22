# Operadores in (entre) e not in(não entre)
# Strings são iteráveis

nome = 'Otávio'
print(nome[1])

# print('i' in nome)
# print('z' in nome)
# print('vio' not in nome)

nome = input('Digite seu nome:')
encontrar = input('Digite o que deseja encontrar no seu nome:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')