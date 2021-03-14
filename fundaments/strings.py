name, inOperator, my_name, trim = 'UserPython','Python','Felipe', ' JÚLIA '

question = input('Digite seu nome completo: ')
print(name[0])
print(name[1])

# Slice
# ':' é até o final/começo/entre da string

print(name[0:4]) # User

print(name[4:]) # Python 
print(name[:4]) # User

print(name[:]) #UserPython


# Tamanho da string (.length)

print(len(name)) # 10
print(len('Felipe')) # 6


# Checando string -> Boolean

print('Python' in inOperator)
print('Python' not in inOperator)
print('Javascript' not in inOperator)


# Metódos para str

print(my_name.lower()) # Lowercase
print(my_name.upper()) # Uppercase
print(trim.strip().lower()) # Trim
print(question.title()) # Deixa o ínicio das palavras em uppercase
print(name.index('P')) # Substring