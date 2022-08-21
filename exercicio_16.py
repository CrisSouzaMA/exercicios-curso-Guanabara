import math

# Digite um número do tipo float e imprima seu inteiro.

num = float(input('Digite um numero: '))
numIntCima = math.ceil(num)
numIntBaixo = math.floor(num)

print(f'O número digitado foi {num}, arredondando para cima fica {numIntCima} e arredondando para baixo fica {numIntBaixo}')
