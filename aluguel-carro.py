dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
p = (dias * 60) + (km * 0.15)
print('O preço por {} dias alugados e por {}Km rodados é de R${:.2f}'.format(dias, km, p))
