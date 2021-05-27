'''
  Escopo de Variaveis no Python
''' 

variable = 'Value' # Escopo Global

def func():
  print(variable)

def func2():
  global variable # Forçando a variavel global a ser trocada a todos os locais. MÁ PRÁTICA
  variable = 'Outro valor' # Escopo Local
  print(variable)

def func3(**kwargs):
  if kwargs is not None:
    arg = kwargs.get('arg')
    if arg:
      arg = arg.replace('v','c')
      return arg

def func4():
  print(variable) # Erro!!!!
  variable = 1234
  print(variable)

func4()
# func()
# func2()
# other_variable = func3(arg=variable)
# print(other_variable) # Outro calor

# print(variable)