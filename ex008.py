#
#
#                   Algoritmo que leia um valor em metros e exiba na tela
#                    o mesmo valor convertido em centimetros e milimetros
#
#
meters = float(input('Digite o valor em metros: '))
print('O valor corresponde a:\nquilômetros: {}.\nhectômetro: {}.\nDecâmetro: {}.\nMetros: {}.'.format(meters/1000, meters/100, meters/10, meters))
print('decimetros: {}.\ncentímetros: {}.\nmilímetros: {}.'.format(meters*10, meters*100, meters*1000))
