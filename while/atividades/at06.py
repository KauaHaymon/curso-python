# ATIVIDADE 6

# SOMA DOS NÚMEROS IMPARES E PARES

contador = 1 
somap = 0
somai = 0
valor = 0

while valor <= 1000:
  valor = int(input('Digite um valor: '))

  if valor > 1000: 
    break
  elif valor%2 == 0:
    somap += valor
  else:
    somai += valor

contador += 1
print('Soma do par é:', somap)
print('Soma do impar é:', somai)