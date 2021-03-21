'''
  Listas sao os arrays
'''
#           0    1    2    3    4
arrays_ = ['A', 'B', 'C', 'D', 'E']

arrays = [1, 2, 3, 4, 'Strings', True, 10.2, False, [1, 2, 3], 'Last']
arrays[5] = False

# Fatiamento
# print(arrays[:3])  # [1,2,3]
# print(arrays[2:])  # [3, 4, 'Strings', False, 10.2, False, [1, 2, 3], 'Last']
# print(arrays[::2])  # Pula de dois em dois
# print(arrays[-len(arrays)])  # 1

l1 = [10, 1000, 2000, 333, 1111, 1000.1, 20, 10, -15]
l2 = [4, 5, 6]
listIterable = list(range(0, 10))
sum_ = 0

l2.append(7)  # Adiciona no final do array (push js)
l2.insert(3, 6.6)  # Insere um valor no indíce 3
l2.pop()  # Remove no final do array
l2.insert(6, 'Banana')
l2.insert(7, 'Maracuja')


del(l2[:2])  # Deleta via índices
# print(l2, sep=" , ")
# print(max(listIterable))  # Pega valor máximo
# print(min(listIterable))  # Pega valor mínino
for v in listIterable:
    sum_ += v

multiTypes = [True, False, 2.0, 2, 'String']

for types in multiTypes:
    print(type(types))


secretValue = 'perfume'
digits = []
changes = 3

while True:
    if changes <= 0:
        print('Você perdeu!')
        break
    letter = input('Digite uma letra: ')
    if len(letter) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue
    digits.append(letter)
    if letter in secretValue:
        print(f'Uhuuuu! A letra {letter} existe na palavra secreta.')
    else:
        print(f'Afsss! A letra {letter} não existe na palavra secreta.')
        digits.pop()

    secretTemp = ''
    for letter_secret in secretValue:
        if letter_secret in digits:
            secretTemp += letter_secret
        else:
            secretTemp += '*'
    print(secretTemp)
    if secretTemp == secretValue:
        print(f'Que legal, você ganhou!!! A palavra era {secretTemp}')
        break
    else:
        print(f'A palavra secreta está assim {secretTemp}')

    if letter not in secretValue:
        changes -= 1
    print(f'Você ainda tem {changes} chances.')
    print()
