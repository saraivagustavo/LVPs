'''Ler 3 valores inteiros (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.'''

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
    if(a > b and a > c):#verifica se a é o maior
        if(b > c):#procurando o segundo maior valor
            print(f'{c} {b} {a}')
        else:
            print(f'{b} {c} {a}')
    else:
        if(b > c):#verifica se b é o maior
            if(a  >c):#procurando o segundo maior valor
                print(f'{c} {a} {b}')
            else:
                print(f'{a} {c} {b}')
        else:#c é o maior
            if(a > b):#procurando o segundo maior valor
                print(f'{b} {a} {c}')
            else:
                print(f'{a} {b} {c}')
    
    return 0

if __name__ == "__main__":
    main()
