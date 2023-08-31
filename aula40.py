# Calculadora com while

while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite a operação (+-/*): ')

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None


    ######### Validações
    if numeros_validos is None:
        print('Digite somente números válidos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    ######### Contas

    print('Realizando sua conta...')
    if operador == '+':
        print(f'Resultado: {num_1_float}+{num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)     
    elif operador == '/':
        print(num_1_float / num_2_float)  
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')


    ############# Função de sair/continuar do programa
    sair = input('[s]air [c]ontinuar ').lower().startswith('s')

    if sair:
        break
    if not sair:
        continue