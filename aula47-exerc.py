"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = 'vasco'
letras_acertadas = ''
tentativas = 0
erros = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    if letra_digitada not in palavra_secreta:
        erros += 1

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            # print(letra_secreta)
            palavra_formada += letra_secreta
        else:
            # print('*')
            palavra_formada += '*'
    print(palavra_formada)

    if tentativas >= 15:
        print('Você tentou muitas vezes. Vamos recomeçar!')
        letras_acertadas = ''
        tentativas = 0

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'Parabéns, você acertou! A palavra secreta era {palavra_secreta.upper()}.')
        print(f'Você tentou {tentativas} vezes.')

        if erros == 0:
            print('Perfeito!! Você não errou nenhuma vez!')
        elif erros == 1:
            print(f'Você errou {erros} vez.')
        elif erros > 1:
            print(f'Você errou {erros} vezes.')
        letras_acertadas = ''
        tentativas = 0
        erros = 0

    