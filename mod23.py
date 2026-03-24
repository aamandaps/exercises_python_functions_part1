#Declarando as variáveis globais
n1:int=0
n2:int=0
n3:int=0
n4:int=0
ordem:int=0

#Inicio

#Procedimento
def ordem():
    #Chamando as variáveis
    global ordem

    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite um valor: '))
    n3 = int(input('Digite um valor: '))
    n4 = int(input('Digite um valor aleatório: '))

    #Verificando a ordem
    if n4<=n1:
        ordem = n4,n1,n2,n3
        print(f'A ordem é:{ordem}')
    elif n4>n1 and n4<=n2:
        ordem = n1,n4,n2,n3
        print(f'A ordem é:{ordem}')
    elif n4>n2 and n4<=n3:
        ordem = n1,n2,n4,n3
        print(f'A ordem é:{ordem}')
    else:
        ordem = n1,n2,n3,n4
        print(f'A ordem é:{ordem}')
    #Fim-condicional
#Fim-procedimento         

#Chamando módulo
def main():
    ordem()
if __name__=="__main__":
    main()
#Fim