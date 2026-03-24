#Declarando as variáveis globais 
v1:int=0
v2:int=0
dif:int=0

#Inicio

#Procedimento
def calc_dif():
    #Chamando as variáveis globais
    global dif 
    global v1
    global v2

    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite um segundo valor: '))

    #Verificando a diferença
    if v1>v2:
        dif = v1-v2
        print(f'A diferença é {dif}')
    else:
        dif = v2-v1
        print(f'A diferença é {dif}')
    #Fim-condicional
#Fim-procedimento

#Chamando o módulo
def main():
    calc_dif()
if __name__=="__main__":
    main()
#Fim