n = 0
s = 0
l = 0

while True:
    n = int (input('Digite um valor: '))
    if n == 999:
        break
    l += 1
    s += n
print(f'Quantidade de numeros digitados: {l} e soma deles vale {s}')