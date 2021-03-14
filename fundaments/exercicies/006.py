n1 = float(input('Digite seu primeiro número: '))
n2 = float(input('Digite seu segundo número: '))

arrayNumbers = [n1,n2]

print(f'O maior número é {max(arrayNumbers)}')

if n1 > n2:
    print('n1 é maior que o n2')
elif n1 == n2:
    print('os dois valores são iguais')
else:
    print('n2 é maior que n1')
