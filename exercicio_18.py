# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

ang = float(input('Digite um ângulo: '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))

print(f'O seno de {ang:.2f} é {sen:.2f}, o cosseno é {cos:.2f} e a tangente é {tang:.2f}')