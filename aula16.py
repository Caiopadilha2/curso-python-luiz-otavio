# if / elif ......... else
# se / se não se .... se não

entrada = input('Você quer "entrar" ou "sair"')

if (entrada == 'entrar'):
    print('Você entrou no sistema')
elif (entrada == 'sair'):
    print('Você saiu do sistema')
else:
    print('Comando inválido! Saindo...')

print('Estou fora do contexto do if')