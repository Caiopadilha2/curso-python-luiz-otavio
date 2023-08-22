# Operadores lógicos
# and(e) - or(ou) - not(não)
# none - não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_valida = 123456

if (entrada == 'E' or 'e') and (senha_digitada == senha_valida):
    print('Entrar')
else:
    print('Sair')


# Avaliação curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)