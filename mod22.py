#Declarando as variáveis globais
n1:int=0
n2:int=0
maior:int

#Inicio

#Procedimento
def calc_maior():
    #Chamando as variáveis
    global maior
    
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))

    #Verificando qual é o maior
    if n1>n2:
        maior = n1
        print
        (f'A ordem é {maior},{n2}')
    else:
        maior = n2
        print(f'A ordem é {maior} e {n1}')
    #Fim-condicional
#Fim-procedimento

#Chamando módulo
def main():
    calc_maior()
if __name__=="__main__":
    main()
#Fim
