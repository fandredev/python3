'''
  While/Else
  contadores
  acumuladores
'''

counter = 1
acumulator = 1

while counter <= 10:
    if counter > 5:
        break  # Break dentro do laço não executa o bloco else
    print(counter, acumulator)
    acumulator = acumulator + counter
    counter += 1

else:
    print('Cheguei no laço else')
