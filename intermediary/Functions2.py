def function(args):
    return args

name = function('Felipe')

if name:
  print(name)
else:
  print('Sem valor retornado da funcao')


######################################################################




def division(n1, n2):
  if n2 == 0:
    return
  return n1 / n2

divisionNumbers = division(8, 2)

if divisionNumbers:
  print(divisionNumbers)
else:
  print('Conta inválida.')



######################################################################




def f(var):
  print(var)

def dumb():
  return f # A função dentro de uma funlão não precisa das 'f()'

var = dumb()('E colocar o meu valor da função f')
varIsCloned = dumb()

print(type(varIsCloned))
print(id(f), id(varIsCloned)) # O mesmo id de memória, ou seja varIsCloned é igual a F
 
if varIsCloned == f:
  print('Var é igual a F')

# dumbed = dumb()

# print(dumbed, type(dumbed))




######################################################################


def withTuple(name, surname):
  return (name, surname)

withTupled = withTuple('Felipe', 'André')

print(f'Seu nome é: {withTupled[0]} {withTupled[1]}')