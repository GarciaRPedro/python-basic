#
#       Algoritmo que lê uma entrada de teclado e exibe informaçoes
#
a = input('Digite algo: ')
print('O valor digitado é do tipo: ',type(a))
print(',É composto só de espaços ?', a.isspace())
print(',É um numero ?',a.isnumeric())
print(',É alfabetico ?',a.isalpha())
print(',É alfanumerico ?',a.isalnum())
print(',Esta em maiusculas ?',a.isupper())
print(',Esta em minusculas ?',a.islower())
print(',Está capitalizada ?', a.istitle())
