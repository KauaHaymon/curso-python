# ATIVIDADE 2
# FILME, DIRETOR E DATA DE LANÇAMENTO


filme = 'Senhor dos Anéis', 'The Batman', 'O iluminado', 'O Chamado', 'Zathura: Uma Aventura Espacial'
diretor = 'Peter Jackson','Matt Reeves', 'Stanley Kubrick', 'Gore Verbinski', 'Jon Favreau'
data = '2001', '2022', '1980', '2002', '2005'

def lin():
  print('-'*30)

for i in range(0,len(filme)):
  print('Filme: ',filme[i])
  print('Diretor: ',diretor[i])
  print('Data de lançamento: ',data[i])
  lin() 