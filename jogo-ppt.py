from random import choice
usu = input('Escolha: Pedra, Papel ou Tesoura? ')
usu = usu.upper()
joke = ['PEDRA','PAPEL','TESOURA']
pc = choice(joke)
print('Computador escolheu {}'.format(pc))
if usu == pc:
    print('EMPATE!')
elif (usu == 'PEDRA' and pc == 'PAPEL') or (usu == 'PAPEL' and pc == 'TESOURA') or (usu == 'TESOURA' and pc == 'PEDRA'):
    print('COMPUTADOR VENCEU!')
elif (usu == 'PEDRA' and pc == 'TESOURA') or (usu == 'PAPEL' and pc == 'PEDRA') or (usu == 'TESOURA' and pc == 'PAPEL'):
    print('PARABÉNS! VOCÊ VENCEU O COMPUTADOR')
else:
    print('Você digitou algo errado! Tente novamente')
