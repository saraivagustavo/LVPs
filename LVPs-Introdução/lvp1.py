'''Faça um programa que leia dois números inteiros e apresente o resultado de sua soma:'''

def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)

    #entrada de dados
    a = int(input("Digite um valor inteiro: "))
    b = int(input("Digite outro valor inteiro: "))

    #processamento de dados
    soma = a + b

    #saída de dados
    print(f'Soma = {soma}')
    return 0
    
if __name__ == "__main__":
    main()