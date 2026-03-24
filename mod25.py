#Declarando as variáveis globais
hora_i:int=0
min_i:int=0
hora_f:int=0
min_f:int=0
hora:int=0
min:int=0

#Inicio

#Procedimento
def calc_jogo():
    #Chamando as variáveis
    global hora_f
    global min_f
    global hora
    global min

    hora_i = int(input('Insira a hora que você começou a jogar: '))
    min_i = int(input('Insira o minuto que você começou a jogar: '))
    hora_f = int(input('Insira a hora que você terminou de jogar: '))
    min_f = int(input('Insira o minuto que você terminou de jogar: '))

    #Verificando se a hora final é menor que a inicial
    if hora_f<hora_i:
        hora_f = hora_f + 24
    #Fim-condicional 1

    #Verificando se o minuto final é menor que o inicial
    if min_f<min_i:
        min_f += 60
        hora_f -= 1
    #Fim-condicional 2

    #Calculando a duração do jogo
    hora = hora_f - hora_i
    min = min_f - min_i

    print(f'A duração foi de {hora}hr e {min}m')
#Fim-procedimento

#Chamando módulo
def main():
    calc_jogo()
if __name__=="__main__":
    main()
#Fim
