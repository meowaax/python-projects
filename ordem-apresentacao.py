from random import shuffle
alunos = []
i = 0
while (i <= 3):
    a = input('Digite o nome do aluno: ')
    alunos.append(a)
    i = i + 1

print(alunos)
shuffle(alunos)

print('O 1° a apresentar é {}'.format(alunos[0]))
print('O 2° a apresentar é {}'.format(alunos[1]))
print('O 3° a apresentar é {}'.format(alunos[2]))
print('O 4° a apresentar é {}'.format(alunos[3]))
