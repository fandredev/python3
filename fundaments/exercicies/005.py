username = input('Digite seu nome: ').strip().title()
age = int(input('Digite sua idade: '))
weight = float(input('Digite seu peso: '))
height = float(input('Digite sua altura:'))

imc = weight / (height*height)    

if imc < 17:
    print(f'O {round(imc)} é muito abaixo do peso atual')
elif 17 <= imc < 18.5:
    print(f'O {round(imc)} é abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'O {round(imc)} é peso normal')
elif 25 <= imc < 30:
    print(f'O {round(imc)} é acima do peso')
elif 30 <= imc < 35 :
    print(f'O {round(imc)} é obesidade I')
elif 35 <= imc < 40 :
    print(f'O {round(imc)} é obesidade II (severa)')
else:
    print(f'O {round(imc)} é obesidade II (severa)')
