'''
  Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números com ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERES)(< ou > ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

'''

num1 = 10
num2 = 3
division = num1 / num2

print(division)  # 3.3333333333335

# .(NÚMERO)f - Quantidade de casas decimais (float)
print('{:.2f}'.format(division))
print(f'{division:.2f}')


name = 'Felipe André'
print(f'{name:s}')  # Especifica explicitamente que é uma string

num_1, num_2, tech = 1, 1150, 'Javascript'

print(f'{num_1:0>10}')  # 0000000001
# 0001150000 - Porque agora usei o operador de centralização
print(f'{num_2:0^10}')

print(f'{num_2:.2f}')  # 1150.00

tech_learning = 'Python'
tech_learning_format = '{:@>7}'.format(tech_learning)
tech_learning_format = '{tl:0<20}'.format(tl=tech_learning)
print(tech_learning_format)
