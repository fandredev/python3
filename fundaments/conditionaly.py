n, u = 10, 20

# if u < n:
#     print(f'{n} é maior que {u}')
#     print('Welcome')
# else:
#     print(f'{n} é menor que {u}')

name = input('Digite seu nome: ')
surname = input('Digite seu sobrenome: ')
age = int(input('Digite sua idade: '))

if age >= 18:
    if len(name) < 6 or len(surname) < 6:
        print('Seu nome ou sobrenome é muito curto')
    else:
        print('Seu nome ou sobrenome é muito longo')
else:
    print('Acesso negado. Você tem menos de 18 anos atualmente.')
    if age == 17:
        print('Falta um ano para acesso ao sistema.')
    else:
        print('Você não tem 17 anos e seu acesso demorará no minino 2 anos.')