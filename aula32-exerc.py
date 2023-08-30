"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

num = input('digitar um número inteiro: ')

# if num_inteiro.isdigit():
#     eh_par = int(num_inteiro) % 2 == 0
#     if eh_par:
#         print('Este número é par')
#     else:
#         print('Este número é impar')
# else:
#     print('Você não digitou um número inteiro')

try:
    num_int = int(num)
    if num_int % 2 == 0:
        print('é par')
    else:
        print('é impar')
except:
    print('Você não digitou um número inteiro')   
    
#######################

horario = input('Digite a hora: ')
horario_int = int(horario)

if (horario_int >= 0) and (horario_int <= 11):
    print('bom dia')
elif (horario_int >= 12) and (horario_int <= 17):
    print('boa tarde')
else:
    print('boa noite')

#######################

first_name = input('Digite seu primeiro nome: ')

if len(first_name) <=4:
    print('Seu nome é curto')
elif len(first_name) == 5 or len(first_name) == 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')