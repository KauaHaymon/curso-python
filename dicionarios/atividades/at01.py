# ATIVIDADE ALUNO, MÉDIA E SITUAÇÃO

dados = {}
dados['aluno'] = str(input('Nome: '))
dados['media'] = float(input('Média: '))

if dados['media']<5:
  print(f'{dados["aluno"]} está REPROVADO!')
  print('Média: ',dados['media'])
elif dados['media']<7:
  print(f'{dados["aluno"]} está de RECUPERAÇÃO!')
  print('Média: ',dados['media'])
elif dados['media']>=7:
  print(f'{dados["aluno"]} está APROVADO!')
  print('Média: ',dados['media'])