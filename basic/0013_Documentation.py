num1 = input('Digite um número: ')
num2 = input('Digite um outro número: ')


# Checa se a variavel contém números e positivos (10, 1000, 1,2,3)

print(num1.isdecimal())
print(num1.isdigit())

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)

except:
    print('Não pude converter os números para realizar contas.')
