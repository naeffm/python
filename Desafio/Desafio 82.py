lista = []
listapar = []
listaimpar = []

while True:
    ei = int(input('Digite um valor: '))
    if ei % 2 == 0:
        listapar.append(ei)
        lista.append(ei)
    else:
        listaimpar.append(ei)
        lista.append(ei)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N ')).upper()
    if resp == 'N':
        break

print(lista)
print(listapar)
print(listaimpar)