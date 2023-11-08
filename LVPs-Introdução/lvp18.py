'''Faça um programa, em Python 3.x, que receba dois números inteiros, um em uma variável a e outro em uma variável b. Proceda a troca dos valores das variáveis, de forma que o valor de b passe pra a e vice-versa. Apresente o valor das variáveis a e b, depois da troca.'''

def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    
    #entrada de dados
    a = int(input())
    b = int(input())
    
    #processamento
    temp = a
    a = b
    b = temp
    
    #saída de dados
    print(f'{a} e {b}')
    return 0
    
if __name__ == "__main__":
    main()