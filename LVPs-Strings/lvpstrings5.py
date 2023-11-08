'''Modifique o programa anterior (LVP STRINGS 4)  de modo que a escada seja invertida.'''

def main():
    #declaração de variáveis
    nome = str("")

    #entrada de dados
    nome = input().upper()
    
    #processamento e saída de dados
    for i in range(len(nome), -1, -1): #começa a variável pelo valor completo dela
        print(nome[0:i])

    return 0

if __name__ == "__main__":
    main()
