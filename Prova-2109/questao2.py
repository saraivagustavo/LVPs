'''Dados, como entrada, quatro valores do tipo inteiro, faça um programa, em Python 3.x, que efetue a soma dos TRÊS MENORES valores informados.'''

def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    c = int(0)
    d = int(0)
    
    #entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    
    #processamento
    if(a > b and a > c and a > d):
        print(b + c + d)
    elif(b > a and b > c and b > d):
        print(a + c + d)
    elif(c > a and c > b and c > d):
        print(a + b + d)
    else:
        print(a + b + c)
    return 0
    
if __name__ == "__main__":
    main()