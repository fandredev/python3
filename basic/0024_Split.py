'''
  Split - Dividir uma string - str
'''

string = 'O Brasil é o país do futebol, o Brasil é penta.'
list_1 = string.split(' ')
list_2 = string.split(',')

counter = 0
word = ''

for value in list_2:
    print(value.strip().capitalize())

# for v in list_1:
#     qtd_vezes = list_1.count(v)
#     if qtd_vezes > counter:
#         counter = qtd_vezes
#         word = v

# print(f'A palavra que apareceu mais vezes é "{word}" ({counter})')
