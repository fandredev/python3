'''
  Operator tenário
'''

# logged_user = True
# msg = 'Usuário logado.' if logged_user else 'Usuário precisa fazer login.'

# print(msg)


age = input('Qual a sua idade? ')

if not age.isnumeric():
  print('Você precisa digitar apenas números')
else:
  age = int(age)
  isEighteenYears = (age >=18)
  msgAccess = 'Acesso liberado.' if isEighteenYears else 'Você não pode acessar.'


print(msgAccess)
