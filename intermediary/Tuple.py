# Na tupla não se pode adicionar, remover, mudar valor do índice, editar e etc
# Na lista você pode fazer tudo isso

choice_index = int(input('Digite o indice '))

t1 = (1,2,3,4,'a','luiz') # Meio que um Object.freeze

# Brincadeira rapida
if choice_index <= t1.index('luiz'):
  print(f'Indice digitado: {choice_index} -> Valor do indice: {t1[choice_index]}')
else:
  print('Digite um número menor')


# Iteração
for index, item in enumerate(t1):
  print(f'Indice: {index}')
  print(f'Item {item}')
  print('----------------------------------')


tupleOtherForm = 1,2,3,'luiz'

print(f'Tuple com outra forma, {type(tupleOtherForm)}')

# Tupla Concatenada

impar = (1,3,5)
par = (2,4,6)
imparAndPar = impar+par

print(imparAndPar)


# Destructuing

one, three, five = impar
two, *rest, six = par

print(one, three, five)
print(two, rest, six)

# Multiplicar tupla

multiplyTupla = (3,5) * 2

print(multiplyTupla)


# Convertendo para lista

animals = ('Lion','Bat','Fish','Donkey') # Não posso editar, add, remover
animals = list(animals) # Converti para lista, agora eu posso

animals.append('Chicken')
animals[0] = 'Alligator'

print(animals)