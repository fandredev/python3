'''
  Visão do Professor
'''

numero_inteiro = input('Digite um número inteiro: ')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)
    if numero_inteiro % 2 == 0:
        print(f'O número {numero_inteiro} é par.')
    else:
        print(f'O número {numero_inteiro} é ímpar.')
else:
    print('Isso não é um número inteiro.')


hour_now = input('Digite o horário atual (0-23): ')

if hour_now.isdigit():
    hour_now = int(hour_now)
    if hour_now < 0 or hour_now > 23:
        print('Horário deve estar entre 0 e 23.')
    else:
        if hour_now <= 11:
            print('Bom dia!')
        elif hour_now <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Por favor, digite um horário entre 0 e 23.')


name = input('Digite seu nome: ')
length = len(name)

if length <= 4:
    print('Seu nome é curto.')
elif length <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
