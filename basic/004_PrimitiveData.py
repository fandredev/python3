"""
  Tipos de dados

  str - string -> textos  = 'assim', "Assim"

  int - inteiro -> númericos = 1 0 -2 10 150 -230

  float - real/ponto flutuante = -1.0 3.0 0.0 4.0 10.0 -1420.02

  bool - booleano/lógico - True | False
"""


print('Luiz', type('Luiz'))
print(0, type(0))
print(0.0, type(0.0))
print(True, type(True))
print(10 == 10, type(10 == 10))


print(bool('')) # False
print(bool([])) # False
print(bool(0))  # False



# Type Casting - Converter de um tipo para o outro


print('Luiz ->', type('Luiz'))
print('Luiz ->', type('Luiz'), bool('Luiz')) # true
print('Luiz ->', type('Luiz'), bool('')) # false
print('Luiz ->', type('Luiz'), bool([])) # false
print('Luiz ->', type('Luiz'), bool(0)) # false


print('10', type('10'), type(int('10')))

# print('Olá', int('Olá')) # Error 
print(10, float(10)) # 10.0
print(10.77, int(10)) # 10