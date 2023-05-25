# ATIVIDADE 3
# MEDIA APROVADO E REPROVADO 

n1 = int(input('Nota um: '))
n2 = int(input('Nota dois: '))
media = (n1+n2)/2
if (media >= 7):
  print('Aluno aprovado, nota: ', media)
else:
  print('Aluno reprovado, nota: ', media)