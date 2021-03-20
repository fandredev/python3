'''
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
'''

text = 'Python'
c = 0

for letter in text:
    print(letter)
print('Finish!!!')
for n in range(20, 10, -1):
    print(n)
print('Finish!!!')
for n in range(100):
    if n % 8 == 0:
        print(n)


new_string = ''

for letter in text:
    if letter == 't':
        new_string += letter.upper()
        # continue
    elif letter == 'h':
        new_string += letter.upper()
        # break
    else:
        new_string += letter

print(new_string)
