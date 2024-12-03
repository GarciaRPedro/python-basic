#
#
#                   Algoritmo que leia a o Salario de um funcionario e exiba na tela
#                                 com reajuste de 15% de promoçãp
#
#
salario = float(input('Digite o valor que receberá o reajuste R$: '))
print('O valor de {}, será alterado para {:.2f}, com o aumento de 15%.'.format(salario, salario + salario * 0.15))
