"""
Split e join com list e str
split - divide uma string
join  - une uma string
"""

frase = 'Olha só que coisa interessante'
palavras_frase = frase.split() # Sem parâmetro "quebra" em espaços em branco
print(palavras_frase)

frase2 = 'Caio, vou dividir essa frase nas virgulas'
separado = frase2.split(', ')
print(separado)

frases_unidas = '-'.join(palavras_frase)
print(frases_unidas)
