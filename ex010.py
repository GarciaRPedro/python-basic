#
#
#                   Algoritmo que leia quanto dinheirouma pessoa tem e exiba na tela
#                               quantos dolares ela pode comprar
#
#                                  /////////considere\\\\\\\\\\\\
#                                   -----US$1,00=R$3,27-----
wallet = float(input('Quantos reais você tem na carteira?'))
print('Caso queira trocar todo seu dinheiro em dólares, você terá US$:{:.2f}'.format(wallet/3.27))
