#
#
#                   Algoritmo que leia o comprimento do cateto adjacente e cateto oposto
#                         calcule e exiba na tela o comprimento de sua hipotenusa
#
#
catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
hipot  = catop ** 2 + catad ** 2
print('{:.2f}'.format(hipot ** (1/2)))