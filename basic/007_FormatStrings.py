"""
  f strings sao mais ou menos o template string do js
"""

n = 1
periodicDecimates = 3.33333333
name = 'Felipe'
age = 15

print('Olá eu chamei ' + str(n))  # Sem f strings
print(f'Dizima periodica {periodicDecimates}')  # Com f strings sem formatação

print(f'Dízima periodica formatada: {periodicDecimates:.2f}')  # Com f strings com formatação
print('Meu nome é {} e tenho {} anos'.format(name, age))  # Sem f strings com formatação
print('Dízima periodica {:.2f}'.format(periodicDecimates))  # Sem strings com formatação
print('{n} tem {i} anos e seu número de dizima periodica é {im:.3f}'.format(n=name, i=age, im=periodicDecimates))
