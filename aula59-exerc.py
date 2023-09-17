"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []

while True:
    print('Selecione uma opção abaixo: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    # if (opcao != 'i') and (opcao != 'a') and (opcao != 'l'):
    #     print('Por favor, digite uma opção válida')

    if opcao == 'l':
        for indice, produto in enumerate(lista):
            print(indice, produto)
        if len(lista) == 0:
            print('Não há nada na lista no momento.')
    
    elif opcao == 'i':
        item = input('Qual item você deseja inserir à lista?')
        lista.append(item)

    elif opcao == 'a':
        item_apagar = input('Qual item você deseja apagar?')

        if item_apagar in lista:
            lista.remove(item_apagar)
        else:
            print('Este item não pertence à lista.')
    
    else:
        print('Por favor, digite uma opção válida')
    


