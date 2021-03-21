list_ = 'O brasil é penta.'
spaces = list_.split(' ')

names = ['Felipe', 'Juliana', 'Rose']

array = [
    [1, 2, 3, 4],
    [5, 6],
    [7, 8]
]
n1, n2, n3 = names
print(n1)


# for key, value in enumerate(list_):
#     print(key, value)

for key, values in enumerate(array):
    print(key, values, array[key])
