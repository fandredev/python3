# 1

num = input('Digite um número inteiro: ')

if num.isnumeric():
    if int(num) % 2 == 0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é ímpar')
else:
    print('O número não é um inteiro')

# 2

hour = input('Digite a hora atual: ')

if len(hour) == 2 and hour.isnumeric():
    if 0 > int(hour) > 24:
        print('O horário deve estar entre 1 e 24 horas')
    elif 0 <= int(hour) <= 12:
        print('Bom dia!')
    elif 12 <= int(hour) <= 17:
        print('Boa tarde')
    else:
        print('Boa noite')

else:
    print('Algum erro ocorreu. Contate o administrador do sistema.')

# 3

username = input('Digite seu nome: ')

if len(username) <= 4:
    print('Seu nome é curto')
elif 4 < len(username) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
