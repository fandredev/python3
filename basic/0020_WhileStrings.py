# índices da string...

phrase = 'o rato roeu a roupa do rei de roma'  # Iterável
len_phrase = len(phrase)
counter = 0
new_string = ''

input_user = input('Qual letra deseja colocar em maíscula? ')

# while counter < 10:
#     print(counter)
#     counter += 1
# else:
#     print(f'O contador não é menor que 10: O valor agora é {counter}')

# Iteração
while counter < len_phrase:
    letter = phrase[counter]
    if letter == input_user:
        new_string += input_user.upper()
    else:
        new_string += phrase[counter]
    counter += 1
else:
    print('O valor da nova string é {}'.format(new_string))
