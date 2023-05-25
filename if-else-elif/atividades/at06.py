# ATIVIDADE 6
# SALÁRIO SINDICAL (INSENTO, 8%, 12%)

salr = float(input('Qual o seu salário?: '))

desconto12 = (salr*12)/100
desconto8 = (salr*8)/100

umAno12 = (salr+desconto12)*12
umAno8 = (salr+desconto8)*12

if (salr > 2500):
  print('Salário:','R$',salr)
  print('Imposto:','R$',desconto12)
  print('1- Com imposto de 12%: ','R$',salr+desconto12)
  print('2- 12 meses com imposto de 12% ao mês: ','R$',umAno12)  
  print('3- 12 meses sem imposto: ','R$',salr*12)
  print('4- Total de imposto a pagar em 1 ano: ','R$',desconto12*12)  
elif (salr>1200): 
  print('Salário:','R$',salr)
  print('Imposto:','R$',desconto8)
  print('1- Com imposto de 8%: ','R$',salr+desconto8)
  print('2- 12 meses com imposto de 8% ao mês: ','R$',umAno8)  
  print('3- 12 meses sem imposto:','R$',salr*12)
  print('4- Total de imposto a pagar em 1 ano: ','R$',desconto8*12)  
        
else:
  print("isento")