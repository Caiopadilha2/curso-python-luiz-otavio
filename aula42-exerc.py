frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.'

# print(frase.count('Python')) 2

i = 0
qtd_letra_apareceu_mais = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_vzs_letra_atual_apareceu = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_letra_apareceu_mais < qtd_vzs_letra_atual_apareceu:
        qtd_letra_apareceu_mais = qtd_vzs_letra_atual_apareceu
        letra_apareceu_mais = letra_atual

    # print(letra_atual, qtd_vzs_letra_atual_apareceu)

    i += 1

print(letra_apareceu_mais, qtd_letra_apareceu_mais)
