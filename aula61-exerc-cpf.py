"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf = '74682489070'
resultado_digito_1 = 0
nove_digitos = cpf[:9]
# print(nove_digitos) # 746824890

contador_regressivo = 10
somatorio = 0

# for num in nove_digitos:
#     while contador_regressivo > 2:
#         multiplicacao = (num * contador_regressivo)
#         contador_regressivo -= 1
#         multiplicacao.join(multiplicacoes)

#     print(multiplicacoes)

for num in nove_digitos:
    # print((int(num) * contador_regressivo))
    somatorio += int(num) * contador_regressivo
    contador_regressivo -= 1
# print(somatorio) # 301
    

resultado = (somatorio * 10) % 11 # 7

if resultado > 9:
    resultado_digito_1 = 0
else:
    resultado_digito_1 = resultado

print(resultado_digito_1) # 7