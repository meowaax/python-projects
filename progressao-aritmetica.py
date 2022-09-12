from time import sleep
pt = int(input('Insira o primeiro termo de uma PA: '))
r = int(input('Insira a razão dessa PA: '))
st = pt + r
pa = [pt, st]
for c in range(0,8):
    st = st + r
    pa.append(st)
print('CALCULANDO...')
sleep(2)
print(pa)
