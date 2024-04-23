total = 0
produtos1000 = 0
menor = 0
cont = 0

while True:
    nome = str(input('Produtc name: '))
    preco = float(input('Price: R$ '))
    cont += 1
    total = total + preco
    if preco > 1000:
        produtos1000 += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar S/N: ')).upper()
    if resp == 'N':
        break
print(f'{total}')
print(f'{produtos1000}')
print(f'{menor}')