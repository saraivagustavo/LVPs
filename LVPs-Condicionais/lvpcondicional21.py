'''Desenvolva um programa que receba dois valores para efetuar operações matemáticas de acordo com a opção do usuário, 1 para soma, 2 para subtração (do primeiro pelo segundo), 3 para multiplicação, 4 para divisão (do primeiro pelo segundo), 5 para exponenciação (o segundo número será a potência), 6 para  raiz (o primeiro número será o radicando e o segundo o índice). Qualquer valor diferente desse deve retornar uma mensagem de erro. Apresente o resultado da operação.'''

def main():
    operacao = int(0)
    a = float(0.0)
    b = float(0.0)
    
    #entrada de dados 
    operacao = int(input("Digite a operação desejada (1 a 6): "))
    if (operacao >= 1 and operacao <= 6):
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        if(operacao == 1):
            print(f'{a + b}')
        elif(operacao == 2):
            print(f'{a - b}')
        elif(operacao == 3):
            print(f'{a * b}')
        elif(operacao == 4):
            print(f'{a / b}')
        elif(operacao == 5):
            print(f'{a ** b}')
        elif(operacao == 6):
            print(f'{a ** (1 / b)}')
    else:
        print('OPERAÇÃO INVÁLIDA')
    return 0
    
if __name__ == "__main__":
    main()