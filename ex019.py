#
#
#                   Algoritmo que leia o nome de quatro alunos e exiba na tela
#                                aleatoriamente o nome de um deles
#
#
import math
import random

name1 = str(input('Digite o nome do primero aluno(a): '))
name2 = str(input('Digite o nome do segundo aluno(a): '))
name3 = str(input('Digite o nome do terceiro aluno(a): '))
name4 = str(input('Digite o nome do quarto aluno(a): '))
alunos = (name1, name2, name3, name4)
escolhido = (random.choice(alunos))
print ('O aluno escolhido para apagar o quadro foi o: {}'.format(escolhido))
