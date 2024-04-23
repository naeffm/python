n1 = int(input('Digite o primeiro valor: '))
n2 = n1
f = 1
print('Calculando {}! = ' .format(n1), end='')
while n2 > 0:
    print('{}'.format(n2), end='')
    print(' x ' if n2 > 1 else ' = ', end='')
    f *= n2
    n2 -= 1

print(f)


