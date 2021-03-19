'''
  Condições IF, ELIF E ELSE
''' 

if False:
    print('Verdadeiro')
elif True:
    print('Estou no elif')
    name = input("What's your name? ")
    print('Your name is {0}'.format(name))
elif False:
    print('Elif nao executado')
else:
    print('A minha expressao nao é verdadeira')