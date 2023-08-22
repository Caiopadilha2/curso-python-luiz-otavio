"""
Peça ao usuário para digitar nome e idade
Se nome e idade foram digitados:
    Exiba:
        seu nome é 
        seu nome invertido
        seu nome tem N letras
        A primeira letra do seu nome é
        A última letra do seu nome é
Se nada for digitado:
    Exiba:
        "Desculpe, você deixou campos vazios.
"""

nome_usuario = input('Digite seu nome: ')
idade_usuario = input('Digite sua idade: ')

nome_sem_espacos = nome_usuario.replace(' ','')

if nome_sem_espacos and idade_usuario:
    print(f'Seu nome é {nome_usuario}')
    print(f'Seu nome invertido é {nome_usuario[::-1]}')
    print(f'A primeira letra do seu nome é {nome_usuario[0]}')
    print(f'A última letra do seu nome é {nome_usuario[-1]}')
    print(f'Seu nome contém {len(nome_sem_espacos)} letras')

    if ' ' in nome_usuario:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
else:
    print('Desculpe, você deixou campos vazios.')