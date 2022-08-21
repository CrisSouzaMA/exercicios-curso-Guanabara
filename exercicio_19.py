# O professor quer sortear um dos seus 4 alunos para apagar o quadro.
# Faça um programa que ajude ele lendo os nomes e escolhendo um aluno.

import random

lista_alunos = []
al1 = str(input('Nome do primeiro aluno: '))
al2 = str(input('Nome do segundo aluno: '))
al3 = str(input('Nome do terceiro aluno: '))
al4 = str(input('Nome do quarto aluno: '))

lista_alunos.append(al1)
lista_alunos.append(al2)
lista_alunos.append(al3)
lista_alunos.append(al4)

aluno_sorteado = random.choice(lista_alunos)

print(f'O aluno que vai apagar o quadro é {aluno_sorteado}')