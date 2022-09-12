v = float(input('Digite o valor a ser sacado: '))
saldo = 1000.00
op = 1
while op != 0:
    if v <= 0:
        print('Valor inválido para saque.')
        break
    if v > saldo:
        print('Seu saldo é de R$ {:.2f}. Impossível sacar R$ {}'.format(saldo, v))
    else:
        saldo = saldo - v
        print('Saque concluído com sucesso! Saldo restante: R$ {:.2f}'.format(saldo))
    op = int(input('Deseja realizar outro saque? Digite 1 para SIM e 0 para NÃO \n'))
    if op == 1:
        v = float(input('Digite o valor do novo saque: '))
    elif op != 1 and op != 0:
        print('Valor inválido.')
        break
print('PROGRAMA ENCERRADO')
