numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis','sete','oito','nove', 'dez','onze','doze','treze','quatoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:
    qual = int(input('Digite um numero de 0 á 20: '))
    if 0 <= qual <= 20:
        break
    print('tente novamente')

for cont in range(0, len(numero)):
    if qual == cont:
        print(f'Você digitou o numero {numero[qual]}')

