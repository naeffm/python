n = int(input('Digite um numero de 1 a 9999 '))
num = str(n)
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Esta é a unidade {}' .format(u))
print('Esta é a unidade {}' .format(d))
print('Esta é a unidade {}' .format(c))
print('Esta é a unidade {}' .format(m))

#print('Esta é a unidade {}' .format(num[3]))
#print('Esta é a dezena {}' .format(num[2]))
#print('Esta é a centena {}' .format(num[1]))
#print('Este é o milhar {}' .format(num[0]))



