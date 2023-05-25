# ATIVIDADE 2
#ATIVIDADE FATORIAL

# criar um programa para solicitar 10 valores inteiros do usuário, calcular o fatorial destes valores e exibir o resultado de cada fatocial.
# Obs: utilizar o modulo math para o desenvolvimento do programa.

from math import factorial
for c in range(10):
  vi = int(input('Digite um valor inteiro: '))
  fator = factorial(vi) 
  print(fator)