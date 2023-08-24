"""
Repetições - While
Executa enquanto uma condição for verdadeira
"""
condicao = True

# while condicao:
#     print(1)
#     print(2)

while condicao:
    nome = input('Seu nome: ')
    if nome != 'sair':
        print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Eu saí do while')


