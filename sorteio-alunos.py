import random
alunos = []
i = 0
while (i <= 3):
    a = input('Digite o nome do aluno: ')
    alunos.append(a)
    i = i + 1

print('-' * 20)
print('O aluno sorteado foi:' + alunos[random.randrange(len(alunos))])

# Outro jeito de fazer:
# escolhido = random.choice(lista)
# cri-se outra variável para receber o nome escolhido
