import random 

numeros = (1,2,3,4,5,6,7,8,9,10)
sorteioo = list()
par = list()

def sorteio():
    for c in range(0,5):
        sorteioo.append(random.choice(numeros))
    print(sorteioo)

def somapar():
    for p in sorteioo:
        if p % 2 == 0:
            par.append(p)
    s = sum(par)
    print(s)

sorteio()
somapar()