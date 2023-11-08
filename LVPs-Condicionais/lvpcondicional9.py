'''Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos dois maiores valores.'''

def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    c = int(0)
    
    #entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())
    
    #processamento
    if (a > b and a > c): #verifica se a é o maior
        if (b > c): #procurando o segundo maior valor
            soma = a + b
        else:
            soma = a + c
    elif(b > c): #verifica se b é o maior
        if(a > c): #procurando o segundo maior valor
            soma = b + a
        else:
            soma = b + c
    elif(a > b): #procurando o segundo maior valor
        soma = c + a
    else:
        soma = c + b
        
    #saída de dados
    print(f'{soma}')
    return 0

if __name__ == "__main__":
    main()
