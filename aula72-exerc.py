# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    somatorio = 1
    for numero in args:
        somatorio *= numero
    return somatorio

total = multiplica(1, 10, 2, 20)
print(total)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(numero):

    par = numero % 2 == 0
    if par:
        return 'Par'
    return 'Impar'

print(par_ou_impar(3))