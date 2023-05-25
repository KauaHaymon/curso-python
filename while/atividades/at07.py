# ATIVIDADE 7

# URNA ELEITORAL

print('************************************')
print('Urna eleitoral eletronica')
print('************************************')

contador=1
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0 
nulo = 0
branco = 0
votos = 1
while (votos > 0): 
  votos = int(input("Digite o número do candidato: "))
  if (votos == 1):
    cand1=cand1 + votos
  elif votos == 2:
    cand2=votos + votos
  elif votos == 3:
    cand3=cand3 + votos
  elif votos == 4:
    cand4 + votos  
  elif votos == 5:
    nulo= nulo + votos
  elif votos == 6:
    branco = branco + votos
  else:
    votos == 0
    break;
contador = contador + 1
print('votos no candidato 1: ',cand1)
print('votos no candidato 2: ',cand2)
print('votos no candidato 3: ',cand3)
print('votos no candidato 4: ',cand4)
print('quantidade de votos nulos: ',nulo)
print('quantidade de votos brancos: ',branco)