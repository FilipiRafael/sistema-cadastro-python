from lib import interface
from lib.arquivo.__inity__ import arquivoExiste, criar_arquivo, ler_arquivo, cadastrar
from time import sleep
import __inity__

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criar_arquivo(arq)

while True:
    user = interface.programa(['VER PESSOAS CADASTRADAS', 'CADASTRAR UMA NOVA PESSOA', 'SAIR DO SISTEMA'])
    if user == 1:
        # Listar conteúdo do arquivo das pessoas cadastradas
        ler_arquivo(arq)
    elif user == 2:
        # Cadastrar uma nova pessoa no arquivo
        interface.menu('NOVO CADASTRO')
        nome = str(input('Nome: ')).title().strip()
        idade = __inity__.leiaInt('Digite a idade: ')
        cadastrar(arq, nome, idade)
    elif user == 3:
        interface.menu('\033[1;36mSaindo do sistema. Até logo!\033[m')
        break
    else:
        interface.menu('\033[1;31mOpção inválidade, digite novamente!\033[m')
    sleep(2)
        
    