'''Faça um programa que escreva na tela os números pares de 0 até 10 (inclusive).'''

def main():
    #declaração de variáveis
    numero = int(0)
    
    i = 0 #inicialização da variável de controle
    #processamento
    while(i <= 10): #condição de parada
        resto = i % 2
        if(resto == 0):
            print(i)
        i = i + 1 #atualização da variável de controle
    return 0
    
if __name__ == "__main__":
    main()
