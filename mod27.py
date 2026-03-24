#Declarando as variáveis globais
num_volta:int=0
metros:float=0.0
tempo:int=0

#Inicio

#Procedimento com passagem de parâmetros
def calc_vel(a,b,c):
    
    vel_media:float=0.0 #Variável local

    #Calculando a velocidade média baseada no número de voltas
    if a>1:
        b *= a
        b /= 1000
        c /= 60
        vel_media = b/c
    else:
        b /= 1000
        c /= 60
        vel_media = b/c
    #Fim-condicional
    
    print(f'A velocidade percorrida foi de: {vel_media} km/h')
#Fim-procedimento


def main():
    #Chamando as variáveis
    global num_volta
    global tempo
    global metros

    #Recebendo os valores do parâmetros
    num_volta=int(input('Digite o números de voltas percorridas: '))
    metros=float(input('Digite quantos metros foram percorridos: '))
    tempo=int(input('Digite o tempo do percurso(em minutos): '))

    #Chamando o módulo
    calc_vel(num_volta,metros,tempo)
main()
#Fim