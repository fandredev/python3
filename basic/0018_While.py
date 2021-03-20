'''
  While em python
'''

# while True:  # Infinity loop
#     name = input('Qual o seu nome? ')
#     print(f'Olá {name.strip()}')
# print('Nao vai ser executado')

# x = y = 0
#
# while x < 10:
#     y = 0
#     while y < 5:
#         print(f'({x},{y})')
#         y += 1
#     x += 1
# print('Finalizou')


# while x < 10:
#     if x == 3:
#         x += 1
#         continue  # o número 3 vai ser pulado
#     elif x == 5:
#         break  # O programa irá sair do loop no número 5

#     print(x)
#     x += 1
# print('Terminou')


while True:
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')
    operator = input('Digite o operador: ')
    quitProgram = input('Deseja sair do programa? [s]im ou [n]ão: ')

    if quitProgram.startswith('s'):
        break

    if not n1.isnumeric() or not n2.isnumeric():
        print('Você precisa digitar um número.')

    num1 = int(n1)
    num2 = int(n2)
    if operator == '+':
        print(num1+num2)
    elif operator == '*':
        print(num1*num2)
    elif operator == '/':
        print(num1/num2)
    elif operator == '-':
        print(num1-num2)
    else:
        print('Operador inválido')
