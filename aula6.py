# Conversão de tipos, coerção
# é o ato de converter um tipo em outro

print(1 + 1) # é dinamica, ele sabe que isso é um int

print('a' + 'b') # concatenou, polimorfismo do sinal +

# print('1' + 1) # TypeError: can only concatenate str (not "int") to str
# Ele não sabe o que fazer, a tipagem é forte, não é fraca igual javascript
print(int('1') + 1)
print(float('1') + 1)

print(bool(''))

print(str(11) + 'b')

# str, int, float, bool: imutaveis


