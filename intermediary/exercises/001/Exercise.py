'''
1 - 
'''
def salutation(greeting, name):
  if greeting and name:
    print(greeting, name, sep=' ')

salute = salutation(name='Felipe', greeting='Olá')


'''
2 -
'''
def sumNumbers(n1, n2, n3):
  if n1 and n2 and n3:
    print(n1 + n2 + n3)
  
sum = sumNumbers(10,10,30)


'''
3 -
'''

def percentNumber(number, percent):
  if isinstance(number, int) and isinstance(percent, float):
    return number + (number * percent / 100)
  else:
    return 'Valores incorretos.'

percent = percentNumber(300, 10)

print(percent)


'''
4 - 
'''

def fb(number):
  returnValues = ['fizz','buzz','fizzbuzz']
  if isinstance(number, int):
    if number % 3 == 0 and number % 5 == 0:
      return returnValues[2]
    if number % 5 == 0:
      return returnValues[1]
    if number % 3 == 0:
      return returnValues[0]
    return number
  else:
    return 'O valor precisa ser um número'

from random import randint

for i in range(100):
  randomic = randint(0, 100)
  print(fb(randomic))