# def func(arg, arg2):
#     return arg * arg2


# multiply = func(2, 2)
# print(multiply)

a = lambda x, y: x * y
print(a(2,2))


listItems = [ # Quero ordenar
  ['Produto 1', 13],
  ['Produto 2 ', 1222],
  ['Produto 3 ', 13],
  ['Produto 4', 646],
  ['Produto 5', 12212],
]

# 'Arrow Function: () => '
listItems.sort(key=lambda item: item[1]) # Altera lista original


print(sorted(listItems, key=lambda i: i[1], reverse=True)) # não altera lista original
