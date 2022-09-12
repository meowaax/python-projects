import random
n1 = random.randint(0, 5)
print(n1)
print('Pensando...')
print('...')
n2 = int(input('Qual número você acha que o computador pensou? '))
if n1 == n2:
    print('Parabéns! Você advinhou!')
else:
    print('Ah não! Você perdeu :(')
