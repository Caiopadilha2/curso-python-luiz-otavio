
# args é convenção
def soma(*args):
    somatorio = 0
    for numero in args:
        somatorio += numero
    return somatorio
    # print(somatorio)

soma_numeros = soma(5, 2, 5, 7, 3)
soma_numeros2 = soma(50, 22, 15, 9, 3)
print(soma_numeros)
print(soma_numeros2)

numeros = [50, 22, 15, 9, 3]
# igual o iterável sum
# print(sum(50, 22, 15, 9, 3)) Não funciona
print(sum(numeros)) # 99