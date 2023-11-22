'''Faça um Algoritmo para ler um valor inteiro e escrever a tabuada de 1 a 10 do valor lido.'''

def main():
    #declaração de variáveis
    n = int(0)
    i = int(0)
    
    i = 1 #inicialização da variável de controle
    
    #entrada de dados
    n = int(input("Digite o número: "))
    
    while (i <= 10): #condição de parada
        print(f'{i} x {n} = {i*n}')
        i = i + 1
    return 0
    
if __name__ == "__main__":
    main()