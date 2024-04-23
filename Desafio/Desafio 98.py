def contador(i,f,p):
    print(f'O contador irá contar de {i} até {f} pulando de {p}.')
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        
    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
    
    print(f'FIM')

contador(1,10,1)
contador(10,0,2)

print(f'agora crie a sua contagem meu amigo')
ini = int(input('inicio: '))
fim = int(input('fim: '))
pula = int(input('pula de quanto: '))

contador(ini,fim,pula)