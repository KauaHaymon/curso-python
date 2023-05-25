# ATIVIDADE 4
# Gratificação de 5% e Imposto de 7%

sal = float(input('Qual o seu salário?: '))
incr = 5*sal/100
tax = 7*sal/100
new = (sal+incr)-tax
print('Seu salário com gratificação de 5% e imposto de 7% é: ',new,'reais.') 