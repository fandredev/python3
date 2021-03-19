# Sistema simples usando operadores


user = input('Nome do usuário: ')
password = input('Senha do usuário: ')

usuario_bd = 'felipepy_'
password_bd = 'pyfelipe_'

if user == usuario_bd and password == password_bd:
    print('Seja bem vindo {user}.'.format(user = user))
else:
    print('O usuário "{0}" com a senha "{1}" não está cadastrado no sistema.'.format(user, password))