#
#
#                   Algoritmo que leia a largura e a altura de uma parede e exiba na tela
#                         sua area e a quantidade de tinta necessaria para pinta-la
#
#                                  /////////considere\\\\\\\\\\\\
#                                         1L pinta 2mˆ2
altura = float(input('Digite a altura da parede, em metros: '))
largura = float(input('Digite a largura da parede, em metros: '))
area = altura * largura
print('A sua parede tem uma area de {}m, logo serão necessarios {:.2f} Litros de tinta para pintar toda a parede'.format(area, area/2))


