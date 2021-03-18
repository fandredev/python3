'''
  Criar variaveis para nome (str), idade (int),
  altura (float) e peso (float) de uma pessoa
  Criar variavel com o ano atual (int)
  Obter o ano de nascimento da pessoa (baseado na idade e no atual)
  Obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
  Exibir o texto com todos os valores na tela usando F-Strings (com as chaves)

''' 

name = 'Juliana'
age = 30
height = 1.90
weight = 60
imc = weight / (height * 2)
current_year = 2021
date_nasc = current_year - age

print('{n} tem {a} anos, {h} de altura e pesa {w} kg.'.format(n = name, a = age, h = height, w = weight))
print(f'O IMC de {name} é {imc:.2f}.')
print('{0} nasceu em {1}.'.format(name, date_nasc))