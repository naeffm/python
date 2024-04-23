n = 1

while n != 'M' and n != 'F':
    n = str(input('Qual seu sexo (M/F): ')) .upper()
    if n != 'M' and n != 'F':
        print('Digite uma letra valida')
    else:
        print('Obrigado pela resposta')
print('FIM')