temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input('Qual seu nome: ')))
    temp.append(int(input('Quantos KG você pesa: ')))

    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()

    resp = ' '
    while resp not in 'NS':
        resp = str(input('Você quer continuar S/N: ')).upper()
    if resp == 'N':
        break

print(princ)
print(f'Este é o maior peso {maior} pertence a ', end='')
for p in princ:
    if p[1] == maior:
        print(p[0],end=' ')
print()

print(f'Este é o menor peso {menor} pertence a ', end='')
for p in princ:
    if p[1] == menor:
        print(p[0], end=' ')