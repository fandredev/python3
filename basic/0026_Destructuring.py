cars = ['Ferrari', 'BMW', 'Gol', 'Ford', 'Porsche']

fruits = ['Apple','Limon','Orange']

good, medium, bad = fruits # good = 'Apple', medium = 'Limon', bad = 'Orange'

print(good, medium, bad, fruits) # Apple Limon Orange ['Apple','Limon','Orange']


# n1, n2 = cars  Erro, pois há 3 valores no array, precisaria completar o n3

# Resolvendo erro acima
# *restList continua com o resto dos valores
# lastValue irá pegar o último valor apos o *restList

car1, car2, *restList, lastValue = cars

print(f'Variavel car1 recebe: {car1}')
print(f'Variavel car2 recebe: {car2}')
print(f'Resto do Array: {restList}')
print(f'Último valor do array: {lastValue}')



'''
  Se eu quero apenas os dois primeiros valores sem me importar com o resto
  eu utilizo o *_
'''

dog_breeds = ['Beagle','Basset hound','Poodgle','Akita', 'Dachshund', 'Husky']

beagle, *_, akita, lastValueByHusky = dog_breeds

print(beagle, akita, lastValueByHusky)
print(dog_breeds)
