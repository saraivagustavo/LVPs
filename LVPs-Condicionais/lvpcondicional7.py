'''Ler um valor inteiro e escrever se é positivo ou negativo (só para efeitos desse programa, considere o valor zero como positivo).'''

def main():
    #declaração de variáveis
    numero = int(0)
    
    #entrada de dados 
    numero = int(input())
    
    #processamento de dados
    
    #saída de dados
    if(numero >= 0):
        print('POSITIVO')
    else:
        print('NEGATIVO')
    return 0

if __name__ == "__main__":
    main()
