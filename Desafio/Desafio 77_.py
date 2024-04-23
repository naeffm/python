tupla = ('Hamburguer', 'Suco', 'Pizza', 'Audim')

for p in tupla:
    print(p)
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra)

