'''
  Entrada de dados
  Sempre retorna string
'''

name = input('Qual o seu nome? ')
age = int(input('Qual a sua idade? '))

date_nasc = 2021 - age

print(f'O usuário digitou {name} e sua idade é {age} e sua data de nascimento é {date_nasc}.')
print(f'Tipo da variavel name é {type(name)}')
print(f'Tipo da variavel age é {type(age)}')
print(f'Tipo da variavel date_nasc é {type(date_nasc)}')



# Calculadora de somar

n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')
n2 = int(n2)

print(int(n1) + n2)