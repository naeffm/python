lista = []

while True:
    c = int(input('Digite um valor: '))
    if c not in lista:
        lista.append(c) #nao pensamos em fazer o if para caso não houvesse o mesmo numero, nós adicinioaos direto e erramos
    else:
        print('numero duplicado')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar S/N ? ')).upper()
    if resp == 'N':
        break
print(sorted(lista))