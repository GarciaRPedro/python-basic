#
#
#                   Algoritmo que  pergunte a quantidade de Km percorridos por um carro alugado
#                               e a quantidade de dias pelos quais ele foi alugado
#                                     Calcule o preço a pagare exiba na tela
#
#                                        /////////considere\\\\\\\\\\\\
#                                         1 dia = R$:60 e 1Km = R$: 0.15

distancia = float(input('Digite quantos Kilômetros o carro percorreu:'))
dias = int(input('Digite quantos dias você ficou com o carro: '))
total = (dias * 60) + (distancia * 0.15)
print('Você deve pagar no total:\nR$:{} pelos dias e R${} pela distancia.\nDando um total de R$: {}.'.format(dias * 60, distancia * 0.15, total))

