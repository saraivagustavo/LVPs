'''Faça um algoritmo que escreva na tela os números de 10 até 0.'''

def main():
    #declaração de variáveis
    i = int(0)
    
    #entrada de dados
    i = 10 #inicialização da variável de controle
    
    #processamento + saída de dados
    while(i >= 0): #condição de parada
        print(i)
        i = i - 1  #atualização da variável de controle
        
    return 0
    
if __name__ == "__main__":
    main()