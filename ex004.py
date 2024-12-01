#
#       Algoritmo para "dissecar" uma variavel
#
n1 = input('Digite alguma coisa: ')
print('O valor digitado é do tipo: ',type(n1))
print(',É uma letra ou palavra ?',n1.isalpha())
print(',É composto só de espaços ?', n1.isspace())
print(',É numérico ?',n1.isnumeric())
print(',É alfanumerico ?',n1.isalnum())
