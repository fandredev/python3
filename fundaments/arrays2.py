# Converter tupla para array

tuple_ = (1,3,4,5,6,7)
arrayNumbers = list(tuple_)

print(type(arrayNumbers))


# Criar um range de números

rangedNumbersStart, rangedNumbersEnd = 2000, 2010

print(list(range(rangedNumbersStart, rangedNumbersEnd))) # [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
print(list(range(rangedNumbersStart, rangedNumbersEnd, 2))) # [2000, 2002, 2004, 2006, 2008]


# Converter strings para uma lista (array)

techs = 'Python Javascript PHP'
techsArray = techs.split(' ')
techsArray = techs.split(sep=' ') # Opcional
print(f'Tecnologias : {techsArray}')


# Desempacotamento de array

values = [True, 100, 'Olá Felipe']
_bool, _number, _string = values # True, 100, 'Olá Felipe'

print(_bool, _number, _string)


# Slice de Array

sliced = [True, False, 100, 'Kira', 1.3, [1,2]]

valuesSliced = sliced[1:3] # [False, 100]
newValuesSliced = sliced[3:] #'Kira', 1.3, [1,2]


print(valuesSliced)
print(newValuesSliced)


# Verificar se elemento está contido

letters = ['A','B','C']

print('A' in letters)
print('A' not in letters)