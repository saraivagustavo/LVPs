'''Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere 'P', se seu argumento for positivo, e 'N', se seu argumento  negativo ou 'Z' se for zero.'''

def f_verificacao(numero):
    if(numero > 0): #verifica se é positivo
        argumento = "P"
    elif(numero < 0): #verifica se é negativo
        argumento = "N"
    else: #verifica se é igual a zero
        argumento = "Z"
    return argumento

def main():
    #declaração de variáveis
    numero = int(0)
    resultado = str("")

    #entrada de dados
    numero = int(input("Digite um número: "))
    
    #invocação da função
    resultado = f_verificacao(numero)
    
    #saída de dados
    print(f'Esse número é: {resultado}')
    print(f'P: Positivo')
    print(f'N: Negativo')
    print(f'Z: Zero')
    return 0
    
if __name__ == "__main__":
    main()