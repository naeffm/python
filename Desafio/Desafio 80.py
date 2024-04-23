list = []

for c in range (0,5):
    valor = int(input('digite um valor: '))
    if c == 0 or valor > list[-1]:
        list.append(valor)
    else:
        pos = 0
        while pos < len(list):
            if valor <= list[pos]:
                list.insert(pos,valor)
                break
            pos += 1
print(list)