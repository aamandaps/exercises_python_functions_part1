#Declarando as variáveis globais
n1:float=0.0
n2:float=0.0
n3:float=0.0
n4:float=0.0
media:float=0.0

#Inicio

#Procedimento
def calc_media():
    #Chamando as variáveis
    global media

    n1 = float(input('Insira a primeira nota: '))
    n2 = float(input('Insira a segunda nota: '))
    n3 = float(input('Insira a terceira nota: '))
    n4 = float(input('Insira a quarta nota: '))

    media = (n1+n2+n3+n4)/4

    #Calculando a média
    if media>=6.0:
        print(f'Aluno aprovado, média = {media:.1f}')
    elif media>3.0 and media<6.0:
        print(f'Aluno deverá realizar o exame, média = {media:.1f}')
    else:
        print(f'Aluno retido, média = {media:.1f}')
    #Fim-condicional
#Fim-condicional

#Chamando módulo
def main():
    calc_media()
if __name__=="__main__":
    main()
#Fim