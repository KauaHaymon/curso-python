# CALCULAR OS NÚMEROS EM QUADRADO

valores = [1,2,3,4,5]

def quadrado(valores):
  quadrado = list()
  for i in valores:
    quadrado.append(i**2)
  return quadrado

resultado = quadrado(valores)
for y in resultado:
  print(y)