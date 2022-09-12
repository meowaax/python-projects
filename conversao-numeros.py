n = int(input('Insira um número inteiro: '))
conv = int(input('ESCOLHA A BASE DE CONVERSÃO: \n(1) BINÁRIO\n(2) OCTAL\n(3) HEXADECIMAL\n'))
if conv == 1:
    print('{} convertido para binário é {}'.format(n, bin(n)[2:]))
elif conv == 2:
    print('{} convertido para octal é {}'.format(n, oct(n)[2:]))
elif conv == 3:
    print('{} convertido para hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('OPÇÃO INVÁLIDA')
