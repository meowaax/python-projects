v = float(input('Qual o valor da casa que deseja-se comprar? '))
s = float(input('Qual é o seu salário? '))
a = int(input('Em quantos anos você gostaria de dividir o pagamento? '))
p = v / (a * 12)
s2 = 0.30 * s
if p > s2:
    print('EMPRÉSTIMO NEGADO! \nParcelas de R$ {:.2f} excedem os 30% do salário permitido: R${:.2f}'.format(p, s2))
elif p <= s2:
    print('EMPRÉSTIMO APROVADO!')
