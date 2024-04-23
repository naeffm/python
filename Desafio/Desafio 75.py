c = 0
tupla = (int(input('primeiro: ')), int(input('segundo: ')), int(input('terceiro: ')), int(input('quarto: ')))

print(tupla, end=' ')

print(tupla.count(9))

print(tupla.index(3))

for n in tupla: #para cada numero na tupla...
    if n % 2 == 0:
        print(n, end=' ')