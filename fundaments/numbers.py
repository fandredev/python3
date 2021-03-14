x = y = 10 # Int
y = 10.5 # Float

strY = '10.5'

print(type(float(strY)))

print(type(x))
print(type(y))


aged = input('Digite sua idade: ') # input() retorna string
print(type(aged))

# Convertendo...

aged_int = int(input('Digite sua idade: '))
print(type(aged_int))

weight = float(input('Digite seu peso: '))
print(type(weight))


print(float(100)) # Convertendo int para float
print(int(100.3)) # Convertendo float para int