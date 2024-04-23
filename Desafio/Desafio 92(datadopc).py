from datetime import datetime
dados = dict()

dados['nome'] = str(input('nome: '))
nascimento = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('cartira de trabalho: '))

if dados['ctps'] > 0:
    dados['contratado'] = int(input('ano de contratação: '))
    dados['aposentadoria'] = (35 - (2023 - dados['contratado'])) + dados['idade']
    dados['salario'] = float(input('salario: R$ '))
    for c,v in dados.items():
        print(f'{c} {v}')
else:
    print('='*50)
    for c,v in dados.items():
        print(f'{c} tem um valor de {v}')
