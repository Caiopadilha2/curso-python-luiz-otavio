"""
INTRODUÇÃO
Try/except -> try/catch

tentar / capturar

"""

# print(123)
# print(456)
# # int('a')  # -> Exceção, código para aqui
# print(789)

numero_str = input('Vou dobrar o n que você digitar: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# Se não conseguir transformar para float, ele pula da linha 18 para a 22



