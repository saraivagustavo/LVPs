'''Faça um programa que leia dois números inteiros, a e b. Se a for maior que b, apresente a soma dos dois, caso a seja menor ou igual a b, apresente o resultado da multiplicação dos dois.'''

def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    soma = int(0)
    produto = int(0)
    
    #entrada de dados
    a = int(input())
    b = int(input())
    
    #processamento
    soma = a + b
    produto = a * b
    
    #saída de dados
    if (a > b):
        print(soma)
    else:
        print(produto)
    return 0

if __name__ == "__main__":
    main()
    