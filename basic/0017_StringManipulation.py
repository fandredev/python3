'''
  Manipulando Strings

* Strings Indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in, len, abs, type, print, etc

Essas funções podem ser usadas diretamente em cada tipo.

'''
# Indices positivos [0-9]
text = 'Python s2'
# Indices negativos -[0-9]

print(text[-9])  # P
print(text[7])  # 8


new_str = text[2:6]  # thon
startsZero = text[:6]  # Python
startsFinish = text[7:]  # s2
negativeIndexes = text[-2:]  # s2
negativeIndexesAll = text[-9:]  # Python s2
cutNegativeIndex = text[:-2]  # Python
jumpLetters = text[::2]  # Vai pular de 2 em 2
jumpLettersIndexes = text[:6:3]  # Vai pular de 2 em 2 e parar no indice 6

print(new_str)
print(startsZero)
print(startsFinish)
print(negativeIndexes)
print(negativeIndexesAll)
print(cutNegativeIndex)
print(jumpLetters)
print(jumpLettersIndexes)
