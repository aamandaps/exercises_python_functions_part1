#Declarando as variáveis globais
v1:float=0
v2:float=0

#Inicio

 
#Procedimento
def calc_maior():
    #Chamando as variáveis
    global v1
    global v2

    v1=float(input('Insira um valor real: '))
    v2=float(input('Insira outro valor real: '))

    #Verificando qual é maior
    if v1>v2:
        print(f'O maior é {v1}')
    else:
        print(f'O maior é {v2}') 
    #Fim-condicional
#Fim-procedimento

#Chamando o módulo
def main():
    calc_maior()
if __name__=="__main__":
    calc_maior()
#Fim
