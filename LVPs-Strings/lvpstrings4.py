'''Modifique o programa anterior (LVP STRINGS 3) de forma a mostrar o nome em formato de escada.'''

def main():
    #declaração de variáveis
    nome = str("")

    #entrada de dados
    nome = input().upper()

    #processamento e saída de dados
    for i in range(1, len(nome) + 1):
        print(nome[:i])

    return 0

if __name__ == "__main__":
    main()
