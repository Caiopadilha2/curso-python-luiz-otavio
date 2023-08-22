"""
Formatação básica de strings

.<número de dígitos>f
(Caractere)(><^)(quantidade)

> - Esquerda
< - Direita
^ - Centro
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #Pading à esquerda
print(f'{variavel: <10}') #Pading à direita
print(f'{variavel: ^10}') #Pading centro
print(f'{variavel:0^10}') 


print(f'{1000.35345436436634:.1f}')
print(f'{1000.35345436436634:+,.2f}')
