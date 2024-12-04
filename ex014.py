#
#
#                   Algoritmo que leia a temperatura em graus Cº e exiba na tela
#                                 em Fº Cº e Kº
#
#
C = float(input('Digite a temperatura em graus Cº:'))
F = ((C * 9)/ 5) + 32
print ('A temperaura {}Cº ,equivale a {}Fº .'.format(C, F))
