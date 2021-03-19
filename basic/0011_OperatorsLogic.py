'''
  Operadores lógicos

  and, or, not, in e not in
'''

# name = input('Digite seu nome iniciando com a letra \'F\': ')
# surname = input('Digite seu sobrenome: ')

number = 5

array = (1,2,3,4)



'''
  Operador AND

  # VERDADEIRO E VERDADEIRO = VERDADEIRO
  # VERDADEIRO E FALSO = FALSO

'''
if number > 2 and number >= 5:
    print('Operador AND pegando')


'''
  Apenas um precisa ser verdadeiro

  OPERADOR OR
'''

if number > 2 or number == 10:
    print('Operador OR pegando')


'''
 Nega a operação TRUE

  OPERADOR NOT
'''

if not number != 5:
    print('Operador NOT pegando')

    
'''
 Verifica se um valor esta numa variavel

  OPERADOR IN
'''

if 5 in array.index('5'):
    print('Operador IN pegando')