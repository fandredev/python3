'''
  Operadores lógicos

  and, or, not, in e not in
'''

a = b = 2
c = 3
d = ''
name = 'Felipe André'
system_administrator = 'Guilherme'



# No AND as duas comparações precisam ser verdadeiras

compare = a == b and b < c  # True

# No OR uma das duas comparações precisam ser verdadeiras

compare = a == b or b > c # True
 

print('{0} {1}'.format(a,b))
print(f'Comparação AND: {compare}')
print(f'Comparação OR: {compare}')


# O Not faz a inversão de valores

if not 2 > 1: # False
    print('Sim, 2 é maior que um')
else:
    print('Operador not')

if not d:
    print('Variavel d está vazia')


# O operador IN verifica se algo está contido dentro de uma expressao

if 'qF' in name:
    print('O F contem na variavel name')
else:
    print('Não existe!')


# O operador NOT IN faz a inversão de valores

if 'Guilherme' not in name:
    print('O operador do sistema não está aqui')
else:
    print('O operador do sistema {n} está aqui.'.format(n = system_administrator))