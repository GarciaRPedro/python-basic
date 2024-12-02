#
#
#                   Algoritmo que leia a o preço de um produto e exiba na tela
#                         seu novo preço com 5% de desconto
#
#
preco = float(input('Digite o valor do produto R$:'))
desc = (preco * 0.05)
print('O novo preço do produto com seu desconto de 5% é de R$:{}.'.format(preco - desc))