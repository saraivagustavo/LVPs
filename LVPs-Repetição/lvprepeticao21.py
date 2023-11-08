'''Desenvolva um programa que receba, enquanto o usuário responder sim "s", dois valores para efetuar operações matemáticas de acordo com a opção do usuário, 1 para soma, 2 para subtração (do primeiro pelo segundo), 3 para multiplicação, 4 para divisão (do primeiro pelo segundo), 5 para exponenciação (o segundo número será a potência), 6 para  raiz (o primeiro número será o radicando e o segundo o índice). Qualquer valor diferente desse deve retornar uma mensagem de erro. Apresente o resultado da operação.'''

def main():
    #declaração de variáveis
    flag = str("")
    operacao = int(0)
    a = int(0)
    b = int(0)
    resultado = float(0.0)
    
    #entrada de dados e processamento
    flag = input("Deseja realizar uma operação? <s/n>: ") #variável de controle
    while(flag.upper() == "S"):
        operacao = int(input("Digite a operação desejada (1 a 6): "))
        if (operacao >= 1 and operacao <= 6):
            a = int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            if(operacao == 1): #soma
                resultado = a + b
            elif(operacao == 2): #subtração
               resultado = a - b
            elif(operacao == 3): #multiplicação
                resultado = a * b
            elif(operacao == 4): #divisão
                resultado = a / b
            elif(operacao == 5): #exponenciação
                resultado = a ** b
            elif(operacao == 6): #radiciação 
                resultado = a ** (1 / b)
        else:
            print('OPERAÇÃO INVÁLIDA')
        flag = input("Deseja realizar outra operação? <s/n>: ") #atualização da variável de controle
        
    print(f'{resultado}')
    return 0

if __name__ == "__main__":
    main()
