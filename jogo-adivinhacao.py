import random
n1 = random.randint(0, 10)
print(n1)
print('Pensando...')
print('...')
n2 = c = 0
while n2 != n1:
    n2 = int(input('Qual número você acha que o computador pensou? '))
    print('Tente novamente.')
    c += 1
print('Finalmente acertou! Foram necessárias {} tentativas.'.format(c))
