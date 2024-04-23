tupla = int(input('digite um valor: ')), int(input('digite um valor: ')), int(input('digite um valor: ')), int(input('digite um valor: '))
s = 0

print(tupla.count(9))
print(tupla.index(3))

for cont in tupla:
    if cont % 2 == 0:
        s += 1

print(s)