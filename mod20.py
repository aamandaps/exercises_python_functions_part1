#Declarando as variáveis globais
a:float=0.0
b:float=0.0
c:float=0.0
delta:float=0.0
x1:float=0.0
x2:float=0.0

#Inicio

#Procedimento
def calc_raiz():
    #Chamando as variáveis
    global delta
    global x1
    global x2

    a = float(input('Insira o valor de A: '))
    b = float(input('Insira o valor de B: '))
    c = float(input('Insira o valor de C: '))

    delta = (b**2)-4*a*c

    #Verificando se há raízes
    if delta>0:
        x1 = (-b + (delta**0.5))/ (2*a)
        x2 = (-b - (delta**0.5))/ (2*a)
        print(f'As raízes são {x1:.2f} e {x2:.2f}')
    elif delta==0:
        x1 = (-b/ (2*a)) 
        print(f'A raiz é {x1:.2f}')
    else:
        print('Não há raízes')
    #Fim-condicional
#Fim-procedimento

#Chamando módulo
def main():
    calc_raiz()
if __name__=="__main__":
    calc_raiz()
#Fim