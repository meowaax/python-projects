algo = input('Digite algo:')
print(type(algo))
print('AlfaNumérico: ', algo.isalnum())
print('Alfabético:', algo.isalpha())
print('Decimal:', algo.isdecimal())
print('Lower:', algo.islower())
print('Supper:', algo.isupper())
print('Numérico:', algo.isnumeric())
print('Capitalizada:', algo.istitle())