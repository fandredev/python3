'''
  Funções - def em Python
'''


def sauluteWithParams(msg, name, surname = 'André'):
  print(msg, name, surname)

sauluteWithParams('Olá', 'Felipe') # com parametros


def paramsNomed(param):
  print(param)

paramsNomed(param = 'Paramêtro')


def logicInParam(name):
  named = name.replace('e', '3');
  print(named)

logicInParam('EEEEEEeeeeeee')