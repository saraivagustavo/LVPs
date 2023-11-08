'''Faça um Algoritmo para ler um valor N e imprimir todos os valores inteiros entre 1
(inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO. UTILIZE O COMANDO WHILE.'''

def main():
    #declaração de variáveis
    i = int(0)
    numero = int(0)
    
    #entrada de dados
    i = 1 #inicialização da variável de controle
    numero = int(input())
    
    #processamento + saída de dados
    while(i <= numero): #condição de parada
        print(i)
        i = i + 1  #atualização da variável de controle
        
    return 0
    
if __name__ == "__main__":
    main()