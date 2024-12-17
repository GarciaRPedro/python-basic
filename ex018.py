#
#
#                   Algoritmo que leia um angulo qualquer e mostre na tela
#                      O valor do seno cosseno e tangente desse angulo
#
import math
ang = float(input('Digite um angulo: '))
seno = math.sin(math.radians(ang))
cosen = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print ('O ângulo {}, tem o Seno de {:.2f} \nCosseno de {:.2f} \nTangente de {:.2f}'.format(ang, seno, cosen, tang))