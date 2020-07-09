def leiaInt(valor):
    while True:
        try:
            numero = int(input(valor))
        except (ValueError, TypeError):
            print('\033[1;31mPor favor, digite apenas um número válido.\033[m')
        except KeyboardInterrupt:
            print('Programa finalizado com sucesso!')
        else:
            return numero
            


