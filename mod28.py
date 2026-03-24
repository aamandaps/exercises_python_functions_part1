#Declarando variáveis globais
preco_atual:float=0.0
media:float=0.0

#Inicio

#Procedimento
def calc_preconv(m,pa):

    preco_novo:float=0.0 #Variável local

    #Verificando o preço atual e calculando o preço novo
    if m<500 and pa<30:
        preco_novo = pa*1.10
        #print(f'O novo preço do produto é: {preco_novo:.2f}')
    elif m>=500 and m<1000 and pa>=30 and pa<80:
        preco_novo = pa*1.15
        #print(f'O novo preço do produto é: {preco_novo:.2f}')
    elif m>=1000 and pa>=80:
        preco_novo = pa*0.05
        #print(f'O novo preço do produto é: {preco_novo:.2f}')
    #Fim-condicional
    print(f'O novo preço do produto é: {preco_novo:.2f}')
#Fim-procedimento

def main():
    #Chamando as variáveis
    global preco_atual,media

    #Recebendo os valores dos parâmetros
    media=float(input('Insira a média mensal de vendas desse produto: '))
    preco_atual=float(input('Inisira o preço atual do produto: '))

    #Chamando o módulo
    calc_preconv(media,preco_atual)
main()
#Fim