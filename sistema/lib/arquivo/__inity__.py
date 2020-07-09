from lib.interface import menu

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True



def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')



def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'O arquivo {nome} não pode ser aberto pois não foi encontrado ou não existe.')
    else:
        menu('\033[1mPESSOAS CADASTRADAS\033[m')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print('Nome:', dado[0]) 
            print('Idade:', dado[1])
            print('\033[1;36m-\033[m' * 15)
    finally:
        a.close()

    
def cadastrar(arquivo, nome='<Desconhecido>', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()
    