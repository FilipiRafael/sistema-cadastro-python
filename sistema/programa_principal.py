from lib import interface
from time import sleep

while True:
    user = interface.programa(['VER PESSOAS CADASTRADAS', 'CADASTRAR UMA NOVA PESSOA', 'SAIR DO SISTEMA'])
    if user == 1:
        interface.menu('Opção 1')
    elif user == 2:
        interface.menu('Opção 2')
    elif user == 3:
        interface.menu('\033[1;36mSaindo do sistema. Até logo!\033[m')
        break
    else:
        interface.menu('\033[1;31mOpção inválidade, digite novamente!\033[m')
    sleep(2)
        
    