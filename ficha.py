soma = 0
maior = 0
mv = ''
m = 0
for c in range(1, 5):
    print('---- {}° PESSOA ----'.format(c))
    nome = input('Qual é o seu nome? ')
    idade = int(input('Quantos anos você tem? '))
    sexo = input('Qual o seu sexo? (F/M) ')
    sexo = sexo.upper()
    soma += idade
    if idade > maior and sexo == 'M':
        maior += idade
        mv = nome
    if sexo == 'F' and idade < 20:
        m += 1
print('A média de idade do grupo é {:.2f}\nO homem mais velho se chama {}\nExistem {} mulheres com menos de 20 anos no grupo'.format((soma/4), mv, m))
