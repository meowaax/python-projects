n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = 0
while op != 5:
    op = int(input('Escolha uma opção: \n'
          '[1] somar \n'
          '[2] multiplicar \n'
          '[3] o maior \n'
          '[4] novos números \n'
          '[5] encerrar programa \n'))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, (n1 + n2)))
    elif op == 2:
        print('{} X {} = {}'.format(n1, n2, (n1 * n2)))
    elif op == 3:
        if n1 > n2:
            print('O maior é {}'.format(n1))
        elif n2 > n1:
            print('O maior é {}'.format(n2))
        else:
            print('{} e {} são iguais.'.format(n1, n2))
    elif op == 4:
        n1 = int(input('Insira um novo valor: '))
        n2 = int(input('Insira um segundo novo valor: '))
