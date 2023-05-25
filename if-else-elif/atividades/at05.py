# ATIVIDADE 5 
# PRIMEIRO NÚMERO MAIOR QUE A SOMA DOS OUTROS

n1 = float(input('número um: '))
n2 = float(input('número dois: '))
n3 = float(input('número três: '))
sum = n2+n3
if (n1 > sum):
  print('Maior número:', n1)
else:
  print('Menor número:', n2,'e', n3)