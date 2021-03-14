# Adicionando itens (append)

tops = ['Poppy', 'Gangplank', 'Aatrox']

tops.append('Irelia') # Adiciona 1 ao final do array
tops.append(['Mordekaiser','Darius'])
print(f'Append method: {tops}')


# 'Spread' (extend)

tops.extend(['Fiora','Garen'])

print(f'Spread: {tops}')


# Adicionando itens em uma posição especificada (insert)

junglers = []
junglers.insert(0, 'Lee Sin')
junglers.insert(3, 'Rammus')
junglers.insert(2, 'Udyr')

junglers.insert(0, 'Graves')

# Lee sin agora é a proxima posição
print(junglers)


# Removendo items (remove)

mids = ['Katarina']
mids.remove('Katarina')
mids.append('Veigar')
mids.append('Yone')
mids.append('Yasuo')

print(mids)


# Removendo items com indice (pop)

mids.pop(2) # ['Veigar', 'Yone']
del mids[0] # ['Yone']

print(mids)


# Deleta a variavel e o local de memória (del)
del mids

# print(mids) -> mids is not defined


# Remove todos os elementos da lista

adcs = ['Caitlyn','Miss Fortune','Aphelios']

clearList = adcs.clear()
print(clearList)


# Conta o números de valores no array

timesDiedGame = [10, 20, 30, 30, 30]

print(timesDiedGame.count(30)) # 3


# Reverte ordem da lista

sups = ['Morgana','Thresh', 'Alistar','Braum','Karma','Lulu']
reverse = sups.reverse()

print(reverse)


# Ordenar lista

randomicNumbers = [1,2,10,3,-4,0,20,200]
print(randomicNumbers.sort())