# BIBLIOTECA DATETIME (dia, mês e ano)

from datetime import datetime

dataH=datetime.today()
dataT='{}/{}/{}'.format(dataH.day, dataH.month, dataH.year)

print(dataT)