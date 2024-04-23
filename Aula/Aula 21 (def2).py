print(help(print))


def contador(i,f,p):
    #como fazer uma docstring, adicionar 3 """ no começo e fim.

    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada pelo pai =)

    """
    
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')

contador(2,10,2)

help(contador)
print()
##############################
print('PARAMETROS OPCIONAIS')

def somar(a=0,b=0,c=0): #esse igual é um parametro opcional, se nao declarar la em baixo, ele vale 0 e ir afuncionar normalmente    
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
print()
###############################
print('ESCOPO DE VARIAVEIS')

def teste():
    x = 8 # o 'X' definido dentro de DEF se torna uma varivel local
    print(f'Na função teste, n vale{n}')
    print(f'Na função teste o x vale {x}')

n = 2 # o 'N' definido aqui se torna uma variavel global
print(f'No programa principal o n vale {n}')
teste()
#print(f'No prorgama principal x vale {x}') #codigo nao funciona
print()
print('EXPLICAÇÃO DE ESCOPO')

def teste(b):
    global a #para usar a varivel global, e qualquer alteração aqui muda o global
    a = 8 #variavel local (o a de fora nao tem nada haver com esse são =!)
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5 #variavel global (serve para todo o programa)
teste(a)
print(f'A fora vale {a}')

##############################################
print()
print('RETORNO DE VALORES')

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)

print(f'Os resultados foram {r1},{r2},{r3}')

############################################
print()
print('RESUMAO')

def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2}, {f3}')

print()

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par(num):
    print('É par!')
else:
    print('Não é par')

