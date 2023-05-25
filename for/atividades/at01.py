# ATIVIDADE 1 (for in)
# Ler a idade de 10 alunos e exibir quantos alunos tem idade maior que 20. 
# Calcule e apresente a media de idade destes alunos.

aluno20 = 0
soma = 0
for i in range(4):
  idade = int(input('Idade: '))

  if idade > 20:
    aluno20 = aluno20 + 1
    soma = soma + idade
    media = int (soma / aluno20)

  
print('De 10 alunos, {} tem mais que 20 anos'.format(aluno20)) 
print('Soma dos alunos maiores que 20: {} anos'.format(soma))
print('Média de alunos maiores que 20: {} anos'.format(media))