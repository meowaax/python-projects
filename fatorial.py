num = int(input('Digite um número: '))
c = num
fat = num
while c != 0:
    c = c - 1
    if c == 0:
        break
    fat = (fat) * c
print('Fatorial de {} é igual a {}'.format(num, fat))