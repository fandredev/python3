your_name = input('Digite seu nome: ').strip().title()
your_age = int(input('Digite sua idade: '))

if your_age >= 18:
    print(f'Seja bem vindo ao nosso site {your_name}.')
else:
    print(f'Você não pode acessar nosso site {your_name}.')
