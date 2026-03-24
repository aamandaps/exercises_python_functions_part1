#Declarando as variáveis globais
n:int=0

#Inicio

#Procedimento
def calc_div():
    #Chamando as variáveis
    global n

    n = int(input('Insira um valor: '))

    #Verificando se é divisível por 2 e 3
    if n%2==0 and n%3==0:
        print('É divisível por 2 e 3')
    else:
        print('Não é divisível por 2 e nem por 3')
    #Fim-condicional
#Fim-procedimento

#Chamando módulo
def main():
    calc_div()
if __name__=="__main__":
    main()
#Fim
