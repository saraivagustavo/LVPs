'''Faça um programa que leia um número inteiro e diga se ele é par ou ímpar.'''

def main():
    #declaração de variáveis
    numero = int(0)
    
    #entrada de dados
    numero = int(input("Digite seu número: "))
    
    #processamento
    resto = numero % 2
    
    #saída de dados
    if (resto == 0):
        print(f'{numero} É PAR')
    else:
        print (f'{numero} É IMPAR')
    return 0

if __name__ == "__main__":
    main()