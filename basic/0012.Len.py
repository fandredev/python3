'''
  Len conta caracteres (.length do JS)
'''

user = input('Digite seu usuário: ')
qtd_caracteres = len(user)

print(user, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 5:
    print('Erro!')
    print('Seu usuário "{u}" tem no mínino 5 caracteres.'.format(u = user))
else:
    print('Cadastrado com sucesso')


# Por baixo dos panos, python chamada a função __len__ do construtor
print(user.__len__())

# Int | Float | Bool não tem a função "len"


# print(len(1))  - Erro
# print(len(1.3))  - Erro
# print(len(False))  - Erro