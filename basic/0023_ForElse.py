variable = ['Luiz Otávio', 'Joãozinho', 'Maria']
startsWithJ = False

# for v in variable:
#     if v.startswith('J'):
#         print('Começa com a letra J', v)
#     else:
#         print('Não começa com J', V)

# for v in variable:
#     if v.lower().startswith('j'):
#         startsWithJ = True
# if startsWithJ:
#     print('Existe uma palavra que existe com J')
# else:
#     print('Não existe uma palavra que começa com J')


for v in variable:
    if v.lower().startswith('j'):
        continue
    print(v)
else:
    print('Não existe uma palavra que começa com J')
