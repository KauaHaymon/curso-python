# FUNÇÃO SQRT, TRUNC

# chama a biblioteca, mas não especifica qual função é
import math

num = int(input("digite um numero: "))
# função SQRT
raiz = math.sqrt(num)
print("a raiz quadrada é: ", math.trunc (raiz))


# especifica as funções de math (SQRT, TRUNC)
from math import sqrt, trunc

num = int(input('digite outro numero: '))
raiz = sqrt(num)
print('A raiz quadrada é: ', trunc(raiz))