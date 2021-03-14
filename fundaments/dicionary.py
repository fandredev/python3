# Dicionários são objetos

names = {
  'name': 'PS4',
  'value': 2500,
  'inventory': True,
  'is_saled': True
}
print(names)
print(type(names)) # Dict


# Acessando elementos

print(names['name'])


# Trocando elementos

names['value'] = 3000
print(names['value'])