#nome = input('Qual é seu nome ?')
#print('Prazer em te conhecer {:-^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, produto é {} e a divisão é{:.3f}'.format(s, m, d), end=(' '))
print('Divisão inteira {}, Potência {}'.format(di, e))
