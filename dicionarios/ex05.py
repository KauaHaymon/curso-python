# ESTADO 

estado = dict()
brasil = list()

for c in range(0,3):
  estado['uf']= str(input('Unidade Fedarativa: '))
  estado['sigla']= str(input('Sigla do Estado: '))
  brasil.append(estado.copy()) # estado.copy() - cria uma copia em sequecia dos estados
print(brasil)

for e in brasil:
  for v in e.values():
    print(v)