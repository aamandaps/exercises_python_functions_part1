#Declarando as variáveis globais
v1:int=0
v2:int=0

#Inicio

#Procedimento
def calc_mult():
    #Chamando as variáveis
    global v1
    global v2

    v1=int(input('Digite um valor: '))
    v2=int(input('Digite um valor: '))

    #Verificando se os valores são múltiplos um do outro
    if v1>v2 and v1%v2==0:
        print(f'{v1} é mútiplo de {v2}')
    elif v2>v1 and v2%v1==0:
        print(f'{v2} é mútiplo de {v1}')
    else:
        ('Não são múltiplos um do outro')
    #Fim-condicional
#Fim-procedimento


#Chamando módulo
def main():
    calc_mult()
if __name__=="__main__":
    main()
#Fim
