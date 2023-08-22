"""
Fatiamento de strings
fatiamento [i:f:p] [::]
"""

variavel = 'Olá mundo'
print(variavel[4]) # m

print(variavel[4:]) # mundo
print(variavel[4:-1]) # mund
# ou esse
print(variavel[4:8]) # mund

print(variavel[:5]) # Olá m
print(variavel[-8:-2]) # lá mun

print(len(variavel)) # 9
print(variavel[0:len(variavel)]) # Olá mundo
print(variavel[0:len(variavel):2]) # De 2 em 2 -> Oámno

#Invertida
print(variavel[::-1]) # odnum álO (Vai de 0 ao final, só que contando de trás pra frente)