tupla = ('zero','um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    n = int(input('Digite um numero de 1 a 20: '))
    if n <= 20 and n >= 1:
        break
    else:
        print('tenta de novo')

for pos, tupla in enumerate(tupla):
    if n == pos:
        print(f'Você escreveu o numero {tupla}')




