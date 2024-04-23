def aumentar(p,num=0,sit=False):
    k = p + ((p / 100) * num) 
    if sit==True:
        return f'R${k:.2f}'.replace('.',',')
    else:
        return k

def diminuir(p,num=0,sit=False):
    d = p - ((p / 100) * num)
    if sit==True:
        return f'R${d:.2f}'.replace('.',',')
    else:
        return d

def dobro(p,sit=False):
    dois = p * 2
    if sit==True:
        return f'R${dois:.2f}'.replace('.',',')
    else:
        return dois

def metade(p,sit=False):
    meio = p / 2
    if sit==True:
        return f'R${meio:.2f}'.replace('.',',')
    else:
        return meio

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def reusmo(preço=0,taxaa=0,taxar=0):
    print('-' * 30)
    print('RESUMO DE VALOR ANALISADO'.center(30))   
    print('-' * 30)
    print(f'Preço analisado: {moeda(preço)}')
    print(f'O dobro do preço é: {dobro(preço,True)}')
    print(f'A metade do preço é: {metade(preço,True)}')
    print(f'Com aumento de {taxaa}% temos: {aumentar(preço, taxaa, True)}')
    print(f'Com diminuição de {taxar}% temos: {diminuir(preço,taxar,True)}')
    print('-' * 30)

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha():
            print(f'ERRO "{entrada}" é um preço invalido!')
        else:
            valido = True
            return float(entrada)