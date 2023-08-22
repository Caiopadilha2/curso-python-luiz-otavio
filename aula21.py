# Operadores lógicos
# and(e) - or(ou) - not(não)
# none - não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_valida = 123456

if entrada == 'E' and senha_digitada == senha_valida:
    print('Entrar')
else:
    print('Sair')