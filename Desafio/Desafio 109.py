import moeda

p = float(input('Digite um valor em R$'))

print(f'a metade de {p} é {moeda.metade(p,sit=True)}')
print(f'O dobro de {p} é {moeda.dobro(p,sit=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10,sit=True)}')
print(f'Diminuido 13%, temos {moeda.diminuir(p,13,sit=True)}')