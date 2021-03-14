numbers = [10,20,30,40]
str = ['Olá','Felipe']
bool_ = [True, False ]
mist = [True, '1', [1,2], 10, 1.5 ]


print(type(str)) # List (Array)
print(type(bool_))
print(numbers)
print(mist)



# Acessando valores via índice
names = ['Felipe', 'André', 'Joana', 'Maria',' Mateus']
print(names[0])

# Mudando valores num array
names[0] = 'Cristiana'
print(names[0])

# Indexação negativa

print(names[-1]) # Mateus
print(names[-2]) # Maria
print(names[-3]) # Joana
print(names[-4]) # André
print(names[-5]) # Cristiana


# max, min, sum

num = [31, 39, 40, 20, 50]

print(f'Valor máximo: {max(num)}') # 50
print(f'Valor minino: {min(num)}') # 20
print(f'Tamanho do array: {len(num)}') # 5
print(f'Soma dos valores do array: {sum(num)}') # 180


# Concatenar listas
media, array1, array2 = sum(num) / len(num), [1,2,3], [4,5,6]

union = array1 + array2

print(f'Média {media}')
print(f'Concat lista: {union}')

# Repetir elementos

repeatElements = ['Vou ser repetido']
repeatString = ' Repeat '

print(f'Repetição de elementos no array: {repeatElements*2}')
print(f'Repetição de elementos na string: {repeatString*2}')