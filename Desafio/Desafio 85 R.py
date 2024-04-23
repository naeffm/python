unica = [[],[]]
valor = 0

for c in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        unica[0].append(valor)
    else:
        unica[1].append(valor)
unica[0].sort()
unica[1].sort()
print(unica)