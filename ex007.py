#
#
#       Algoritmo que leia duas notas de um aluno e exiba na tela
#           a sua média geral
#
#
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média entre {:.1f} e {:.1f} é: {:.1f}'.format(nota1, nota2, media))
