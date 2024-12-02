#
#
#       Algoritmo que lê um numero interio e exiba na tela
#           seu dobro, triplo e quadrado
#
#
n = int(input('Digite um número inteiro: '))
print('O dobro de {} é: {}.\nSeu triplo é : {}.\nA raiz quadrada é: {:.2f}.'.format(n, n*2, n*3, n** (1/2)))
