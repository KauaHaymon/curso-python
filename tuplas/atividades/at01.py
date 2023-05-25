# Crie uma tupla para guardar o nome de 3 alunos, em seguida crie uma tupla chamada 'nota' e
# guarde as notas desses alunos.
# Em seguida exiba os nomes e as notas destes alunos.
# em seguida cria uma variavel 'media' e some a media.

import numpy
alunos = 'raquel', 'marcos', 'santander'
nota =(6.7, 2.9, 4.5)
media = (nota)
print('A nota de {} é : {}''\n''A nota de {} é: {}''\n''A nota de {} é: {}'.format(alunos[0], nota[0], alunos[1], nota[1], alunos[2], nota[2]))
print('A media total é: ', numpy.mean(media))
print('A soma da media é: ', sum(media))