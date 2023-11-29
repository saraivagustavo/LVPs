'''Faça um programa, em Python 3.x, UTILIZANDO OBRIGATORIAMENTE COMANDO DE REPETIÇÃO, que solucione o seguinte somatório:
S =  -1/(1+1) + 2/(3+4) - 3/(5+9) + 4/(7+16) ..... - 9/(17+81) + 10/(19+100)'''

def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    c = int(0)
    soma = int(0)
    #inicialização das variáveis
    b = 1
    c = 1
    soma = 0
    #condição de parada
    for a in range(1,11):
        if(a % 2 == 1):
            soma -= a / (b + c)
        else:
            soma += a / (b + c)
        a += 1
        b += 2
        c = a ** 2
    print(soma)
    return 0
    
if __name__ == "__main__":
    main()