# ATIVIDADE 1
# ANO BISSEXTO 

from datetime import datetime

nascimento = datetime(2000,6,10)
anoatual = datetime.now()
dias = abs((datetime.now()-nascimento).days)
anos = dias//365 
meses = dias//30

anoBissexto = anos//4
diasReais = anoBissexto + dias

print(dias,'dias sem anos bissextos')
print(diasReais,'dias com anos bissextos')
print(anos,'anos')
print(meses,'meses')