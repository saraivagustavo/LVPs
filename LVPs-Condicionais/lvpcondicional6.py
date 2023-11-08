'''Elaborar um programa que efetue a leitura de um número inteiro e efetue a sua apresentação, caso o valor não seja divisível por três.'''

def main():
    #declaração de variáveis
    numero = int(0)
    
    #entrada de dados
    numero = int(input())
    
    #processamento de dados
    resto = numero % 3
    
    #saída de dados
    if(resto != 0):
        print(numero)
    else:
        print('')
    return 0

if __name__ == "__main__":
    main()
    