frase = 'Curso em Video Python'

print(frase[15:])

print(frase[9:21])

print(frase[9:21:2]) #vai pular de 2 em 2 entre 9 e 21

print(frase[9::3]) #vai pular de 3 em 3 entre 9 ate o final

print(len(frase)) #mostra o quanto de caracteres vai ter

print(frase.count('o')) #mostra quantos 'o' tem na frase

print(frase.count('o',0,14)) #mostra quantos 'o' tem
                             #ja fatiando de 0 ao 14

print(frase.find('deo')) #aonde que vai começar o 'deo'

print(frase.find('Android')) #o que ele mostra quando nao existe ?

print('Curso' in frase) #Vai dizer se tem ou não

print(frase.replace('Python','Android')) #Substitue a frase que quiser

print(frase.upper()) #deixa tudo em maiusculo

print(frase.lower()) #deixa tudo em minusculo

print(frase.capitalize()) #vai deixar so a primeira em maiusculo

print(frase.title()) #vai transformar em maisculo todo começo de frase

frase2 = '   Aprenda Python  '

print(frase2.strip()) #ele remove os espaços desnecessarios usado por burros

print(frase2.rstrip()) #ele remove os espaços da direita

print(frase2.lstrip()) #ele remove os espaços da esquerda

print(frase.split()) #ele gera uma lista com todas as palabras e contando os espaços
                     #cada quadrado vai ter seu numero

print('-'.join(frase)) #Coloca um '-' em espaços


#você pode mostrar todo o texto sem ter que ir colocando print em toda linha