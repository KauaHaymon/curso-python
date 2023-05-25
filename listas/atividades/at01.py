# ATIVIDADE ZODÍACO CHINÊS 

def lin():
  print('-'*15)

lin()
print('Zodíaco chinês')
lin()

signo = ['Macaco','Galo','Cão','Porco','Rato','Boi','Tigre','Coelho','Dragão','Serpete','Cavalo','Carneiro']
ano=list(range(0,12))

n = int(input('Digite um numero de 0 a 11: '))
for i in range(0,len(signo)):
  if n > 11:
    print('numero não corresponde!')
    break
  
print('\n''O número {} corresponde ao signo {}'.format(ano[n],signo[n])) 