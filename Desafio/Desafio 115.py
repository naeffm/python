import menu
import arquivoo

arq = 'cursoemvideo.txt'

if arquivoo.arquivoExiste(arq):
    print('arquivo encontrado')
else:
    print('arquivo não existe')


while True:
    resposta = menu.alo(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        print('Opção1')
    elif resposta == 2:
        print('opção2')
    elif resposta == 3:
        print('SAINDO DO SISTEMA... ATÉ L O G O')
        break
    else:
        print('ERRO! DIGITE UMA OPÇÃO VALIDA!')
    
