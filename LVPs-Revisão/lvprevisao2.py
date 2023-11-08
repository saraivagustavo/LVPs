'''Faça um programa que, dados 4 números inteiros com entrada, apresenta a soma do maior e do menor valor.'''

def main():
    #delcaração de variáveis
    a = int(0)
    b = int(0)
    c = int(0)
    d = int(0)
    maior = int(0) #implícita
    menor = int(0) #implícita
    
    #entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    
    #processamento
    #condicional para achar o maior valor
    if(a > b and a > c and a > d):
        maior = a
    elif(b > c and b > d):
        maior = b
    elif(c > d):
        maior = c
    else:
        maior = d
     
    #condicional para achar o menor valor   
    if(a < b and a < c and a < d):
        menor = a
    elif(b < c and b < d):
        menor = b
    elif(c < d):
        menor = c
    else:
        menor = d
     
    #saída de dados   
    print(f'{maior + menor}')

    return 0
    
if __name__ == "__main__":
    main()
