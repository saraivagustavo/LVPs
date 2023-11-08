'''Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor.'''

def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    diferenca1 = int(0)
    diferenca2 = int(0)
    
    #entrada de dados
    a = int(input())
    b = int(input())
    
    #processamento de dados
    diferenca1 = a - b
    diferenca2 = b - a
    
    #saída de dados
    if(a > b):
        print(diferenca1)
    else:
        print(diferenca2)
    return 0
    
if __name__ == "__main__":
    main()
    