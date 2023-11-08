'''Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.'''

def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    c = int(0)
    
    #entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())
    
    #saída de dados
    if (a > b and a > c):
        print(a)
    elif(b > c):
        print(b)
    else:
        print(c)
    return 0

if __name__ == "__main__":
    main()