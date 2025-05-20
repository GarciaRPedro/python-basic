"""
frase[x:y:z] = x (recebe o valor inicial do fatiamento), y (recebe o valor final do fatiamento), z (recebe o intervalo da analise )

len(frase) = exibe informações sobre a frase

frase.count('o') = conta quantas vezes o caractere entre aspas aparece na frase

frase.find('deo') = Exibe em que parte foi iniciada o conjunto de caracteres 'deo'

'Curso' in frase = exibe se a palavra existe dentro da frase 

frase.replace("Python','Android') = Procura na string a palavra "Python" e a Substituirá pela palavra "Android"

frase.upper() = transforma toda a string em maiusculo

frase.lower() = transforma toda a string em minuscula

frase.capitalize() = transforma toda a string em minusculo mas mantem o primeiro caractere da primeira palavra em maiusculo

frase.title() = altera a primeira letra de todas as palavras da string para maiuscula

frase.strip() = remove os espaços vazios no inicio e no final da string

frase.rstrip() = remove os espaços vazios no lado direito (no final) da string

frase.lstrip() = remove os espaços vazios no lado esquerdo (no inicio) da string

frase.split() = divide a string a partir dos espaços a partir dos espaços transformandoas em uma lista
com todas as palavras de uma cadeia de caracteres

'-'.join(frase) = reverte o split adicionando um caractere entre as palavras juntando todos os elementos de 'frase'

"""
frase = 'Curso em Video Python'
print(frase[1:15:2])


#ex. 22 crie um programa que leia o nome completo de uma pessoa e mostre :
#- O nome com todas as letras maiúsculas
#- Quantas letras tem ao todo (sem considerar espaços)
#- Quantas letras tem o primeiro nome