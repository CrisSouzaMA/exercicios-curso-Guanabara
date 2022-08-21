# Professor quer sortear a ordem de apresentação dos trabalhos.
# Faça um programa que leia os nomes dos alunos e devolva a lista com a ordem sorteada

from random import shuffle

al1 = str(input('Nome do primeiro aluno: '))
al2 = str(input('Nome do segundo aluno: '))
al3 = str(input('Nome do terceiro aluno: '))
al4 = str(input('Nome do quarto aluno: '))

lista_alunos = [al1, al2, al3, al4]

print('A ordem de apresentação será: ')
print(shuffle(lista_alunos, k=4))