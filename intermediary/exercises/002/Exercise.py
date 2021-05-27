'''
1- 

'''
def main(arg):
  return arg

def sec():
  return 'Valor da funcao 2'

sec = main(sec())
print(sec)


'''
2
'''
def teacher(*args):
  return args

def main2(arg):
  if arg is not None:
    return arg

def sec2():
  return 'Valor da função 2'

_teacher = teacher(main2(sec2()), sec2())
print(_teacher)


# Professor abaixo

def mestre(funcao, *args, **kwargs):
  return funcao(*args, *kwargs)

def fala_oi(name):
  return f'Oi {name}'

def saudacao(name, saudacao):
  return f'{saudacao} {name}'

executando = mestre(fala_oi, 'Luiz')
print(executando)