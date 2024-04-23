def area(largura,cumprimento):
    s = largura * cumprimento
    print(f'A área do seu terreno {largura}x{cumprimento} é {s}m².')


print('CONTROLE DE TERRENOS')
print('-='*20)
largura = float(input('LARGURA (m): '))
cumprimento = float(input('Cumprimento (m): '))
area(largura,cumprimento)
