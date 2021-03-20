# title - Comece as letras com letra maísula
# strip - Trim
# endswith - Comece com x letra
# endswith - Termine com x letra
# isupper - Verifica se a string esta em uppercase
# islower - Verifica se a string esta em lowercase
# replace - Troca uma string por outra


username = input('Digite o nome \'Felipe\': ').title().strip()

# Comece com F e verifique se vai de pos 0 até pos 6
startsWithF = username.startswith('F', 0, 6)

# Termine com E e verifique se vai de pos 0 até pos 6
endsWithE = username.endswith('e', 0, 6)

if startsWithF and endsWithE:
    print(f'Você digitou corretamente, {username}')
else:
    print('Você digitou incorretamente.')


tech = 'python'.upper()
js = 'JAVASCRIPT'.lower()
print(tech)

if tech.isupper():
    print(f'A variavel tech está em uppercase: {tech}')

if js.islower():
    print(f'A variavel js está em lowercase: {js}')


variable = 'apple'.replace('apple', 'limon')
print(variable)
