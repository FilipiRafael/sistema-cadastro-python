import __inity__


def linha(tam=42):
    return '\033[1;35m-\033[m' * tam


def menu(nome):
    print(linha(len(nome)))
    print(nome.center(len(nome)))
    print(linha(len(nome)))


def programa(lista):
    menu('\033[1;36m    MENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha(18))
    opcao = __inity__.leiaInt('Digite a opção desejada: ')
    return opcao