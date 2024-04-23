lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

lanche[3] = 'Picole' #adicionar 'picole' na posição 3 da lista.

lanche.append('coke') # o comando append adicinoa elemento, porem no final.

lanche.insert(0,'kikao') #adicionar o 'kikao' na posição zero sem substituir o hamburguer.

print(lanche)

# tres opções para ser remover algo da lista.

del lanche[3] #o mais normal.
lanche.pop(3) #o pop é geralmente usado para remover o ultimo da lista, mas tambem pode ser usado especificando.

if 'pizza' in lanche:
    lanche.remove('pizza') #para remorer algo especifico sem indicar posição

print(lanche)

print('*' *60)

valores = list(range(4,11)) #fazendo uma lista com range

print(valores)

print('*' *60)

exemplo = [8,2,5,4,9,3,0]

print(exemplo)

exemplo.sort() #coloca todos os valores da lista em ordem

print(exemplo)

exemplo.sort(reverse=True) #ordem inversa

print(exemplo)

print(len(valores)) # para saber quantos elementos tem na lista