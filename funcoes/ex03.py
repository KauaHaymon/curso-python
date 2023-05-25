# NOME E IDADE

def mensagem():
  print('BEM VINDO')
  nome =input('Qual o seu nome? ').strip().title()
  data = int(input('Em que ano nasceu? '))
  dataAtual = 2022
  idade = dataAtual - data
  print('Olá {}, você tem {} anos de idade'.format(nome,idade))

mensagem()