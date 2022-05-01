def saudacao():
    print('''
    ###############
    #  Bem vindo  #
    #     ao      #
    #  Conversor  #
    #     de      #
    # Temperatura #
    ###############''')


def escolha_conversao():
    escolha = input('Digite "C" para converter Farenheint em Celcius e "F" para converter Celcius em Farenheit: ')

    if escolha == 'f' or escolha == 'F':
        converter_F()

    elif escolha == 'c' or escolha == 'C':
        converter_C()

    elif escolha == '':
        print('Digite algo por favor: ')
        escolha_conversao()

    else:
        print('Digite algo correto') 
        escolha_conversao()

def converter_C():

    graus_farenheit = int(input('Digite a temp em Farenheit:'))
    graus_celcius = (graus_farenheit -32) / 1.8
    print(f'{graus_celcius:.2f} Celcius')
    continuar()

def converter_F():

    graus_celcius = int(input('Digite a temperatura em Celcius: '))
    graus_farenheit = (9/5)* graus_celcius + 32
    print(f'{graus_farenheit:.2f} Farenheit')
    continuar()

def continuar():
    
    escolha = input('Deseja continuar as conversões S/N ?')
    if escolha == 's' or escolha == 'S':
        escolha_conversao()
    elif escolha == 'n' or escolha == 'N':
        print('Tchau Tchau Baby!')
    else:
        print('bye')


saudacao()
escolha_conversao()
