import math

co = int(input('Qual o comprimento do cateto oposto '))
ca = int(input('Qual o comprimento do cateto adjacente '))
cal = pow(co,2) + pow(ca,2)

h = math.sqrt(cal)

print('Este é o calculo da hipotenusa {}'.format(h))

#from math import hypot
# ou
# cal= math.hypot(co, ca)