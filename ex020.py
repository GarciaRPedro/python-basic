#
#
#                   Algoritmo que leia o nome de quatro alunos e exiba na tela
#                           aleatoriamente uma ordem com nome o deles
#
#
import random
nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))
nome = (nome1, nome2, nome3, nome4)
ordem = random.sample(nome, k=4)
print('De acordo com os nomes apresentados a ordem será: {}'.format(ordem))