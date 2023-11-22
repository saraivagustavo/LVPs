'''Faça um Algoritmo que escreva na tela os números de 0 até 9.'''

def main():
    #declaração de variáveis
    i = int(0)
    
    #entrada de dados
    i = 0 #inicialização da variável de controle
    
    #processamento + saída de dados
    while(i < 10): #condição de parada
        print(i)
        i = i + 1  #atualização da variável de controle
        
    return 0
    
if __name__ == "__main__":
    main()