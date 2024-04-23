par = []
impar = []
unica = []
usu = 0

for c in range(0,7):
    usu = int(input('Digite um valor: '))
    if usu % 2 == 0:
        par.append(usu)
    if usu % 2 != 0:
        impar.append(usu)

par.sort()
impar.sort()

print(par)
print(impar)

unica.append(par[:])
unica.append(impar[:])
print(unica)