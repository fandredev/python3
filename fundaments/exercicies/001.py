# Escreva um programa que solicite o nome e o sobrenome do usuário.
#  Ao final o programa deverá apresentar o nome completo do usuário na tela.


name, surname = input('Digite seu nome: ').strip().title(), input('Digite seu sobrenome: ').strip().title()

print(f'{name} {surname}')
