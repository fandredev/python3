# Tuplas é um 'array' imútavel.


# Tupla com multiplos valores
tuple_ = (1,2,3,4,5,6)
otherTuple = 1,2,3,4,5,6,6,6,6,6

print(type(tuple_))
print(type(otherTuple))

# Tupla com um único valor

unicTuple = (1,)
otherUnicTuple= 1,

print(type(unicTuple))
print(type(otherUnicTuple))

# Indice da tupla
indexTuple = otherTuple.index(3) # 2

# Contar o número de vezes que o número aparece na tupla

countTupleTime = otherTuple.count(6)

print(f'Indíce da tupla {indexTuple}')
print(f'Vezes que o número aparece: {countTupleTime}')