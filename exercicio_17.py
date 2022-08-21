# Faça um programa que leia a medida do cateto oposto e do cateto adjacente ce um triângulo retangulo e
# calcule e retorne o valor da hipotenusa

from math import hypot

cateto_oposto = int(input('Digite a medida do cateto oposto: '))
cateto_adjacente = int(input('Digite a medida do cateto adjacente: '))
hipotenusa = int(hypot(cateto_oposto, cateto_adjacente))

print(f'A hipotenusa é {hipotenusa}')