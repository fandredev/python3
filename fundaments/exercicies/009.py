cat1 = int(input('Digite um cateto do triângulo: '))
cat2 = int(input('Digite o outro cateto do triângulo: '))
hip = int(input('Digite a hipotenusa do triângulo: '))


if hip == cat1 and hip == cat2 and cat1 == cat2:
    print('Todos os lados possuem o mesmo tamanho: Triângulo equilátero')
elif hip != cat1 and hip != cat2 and cat1 != cat2:
    print('todos os lados possuem medidas diferentes: Triângulo escaleno')
else:
    print('dois lados com o mesmo tamanho: Triangulo isósceles')
