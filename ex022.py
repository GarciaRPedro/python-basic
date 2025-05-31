#
#   ex. 22 crie um programa que leia o nome completo de uma pessoa e mostre :
#- O nome com todas as letras maiúsculas
#- Quantas letras tem ao todo (sem considerar espaços)
#- Quantas letras tem o primeiro nome
#
#

nome = str(input('Digite seu nome\n')) 

print("O seu nome com todas as letras maiusculas é:\n", nome.upper())

print("O seu nome com todas as letras minusculas é:\n", nome.lower())

print(nome.split())

print(''.join(nome))
