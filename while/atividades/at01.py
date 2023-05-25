# ATIVIDADE 1
# JOGO DA ADIVINHAÇÃO

print('***********************************')
print('BEM VINDO AO JOGO DE ADIVINHAÇÃO!!')
print('DICA: dois números iguais menores que 10.','\n')
print('***********************************')
n_secreto = 55
total_tries = 1

while total_tries <= 3:
  chute = int(input('Chute um número: '))
  if chute == n_secreto:
    print('Você acertou! ✌(ツ)','\n','O número secreto é:', n_secreto)
    break
  elif chute < n_secreto:
    print('Você errou, seu chute é menor que o número secreto!','\n')
  elif chute > n_secreto:
    print('Você errou, seu chute é maior que o número secreto!','\n')
  elif chute > total_tries:
        print('Suas tentativas acabaram! ¯\_(ツ)_/¯ ')

total_tries += 1