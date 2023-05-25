# ADICIONAR VALORES NA LISTA (.append) 

dados = list()
continuar = 's'

cont = 0
while cont >= 0:
  dados.append(int(input('Digite um valor: ')))
  continuar=str(input('Você deseja continuar?'))
  if continuar == 'n':
    break
  cont += 1
print(dados)