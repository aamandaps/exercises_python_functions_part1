#Declarando as variáveis globais
valor:float=0.0
tipo:str
poup:str = "poupança"
rend_fixa:str = "renda fixa"

#Inicio

#Procedimento
def calc_rendimento(t,v):
    global poup,rend_fixa
    rend:float=0.0 #Variável local

    #Verificando o tipo de investimento e o rendimento
    if t == poup:
        rend = v * 1.03
    elif t == rend_fixa:
        rend = v * 1.05
    #Fim-condicional

    print(f'O valor atual é: {rend:.2f}')
#Fim-procedimento

def main():
    #Chamando as variáveis
    global tipo,valor

    #Recebendo os valores dos parâmetros
    tipo = (input('Digite o tipo de investimento: '))
    valor = float(input('Digite o valor investido:'))

    #Chamando o módulo
    calc_rendimento(tipo,valor)
main()
#Fim