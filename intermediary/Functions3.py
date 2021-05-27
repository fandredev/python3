'''
  Funções (Def) em Python - *args, **kwargs
'''


# def func(a1, a2, name='Felipe', a3): # Erro, pois o a3 precisa ter um padrao no arg anterior nomeado
#   print(a1, a2, name)

# func(1,2)


def dontKnowParameters(*args): # Os args seram uma tupla
  # args[0] = 20 # Erroo, não posso trocar o parametro
  for v in args:
    print(f'Valor: {v}')
  print(args)
  print(args[0])
  print(args[-1])
  print(len(args))

# dontKnowParameters(1,2,3,4,5)
lista = ['name','surname','value']
# dontKnowParameters(*lista)

# var = dontKnowParameters()

# lista = [1,2,3,4,5]
# n1, n2, *n = lista

# print(n1, n2, n) # 1, 2, [3,4,5]
# print(*lista, sep=",") # 1,2,3,4,5

fruits = ['Apple','Limon']

def kwargs(*args, **kwargs):
  print(args) # Todos os meus argumentos
  print(kwargs) # Todos os meus argumentos nomeados

  animal = kwargs.get('lion') # Melhor maneira de buscar um argumento numa função
  if animal is not None:
    print(animal)
  else:
    print('O argumento lion não existe')

kwargs(*fruits, lion='Lion') 
