# NOME E VALORES

pessoas = {'nome':'kaua','sexo':'Masculino','idade':18}
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos. Seu sexo é {pessoas["sexo"]}.')
for k,v in pessoas.items():
  print(k,'é',v)

for v in pessoas.values():
  print('=-'*5)
  print(v)