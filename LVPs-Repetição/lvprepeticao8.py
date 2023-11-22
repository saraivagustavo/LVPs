'''Faça um algoritmo que leia 5 valores inteiros e escreva no final a soma dos valores lidos.'''

def main():
    #declaração de variáveis
    numero = int(0)
    soma = int(0)
    
    soma = 0 #incialização da variável controladra
    i = 0 #inicialização da variável de controle
    while(i < 5): #condição de parada
        #entrada de dados
        numero = int(input())
        #processamento
        soma = soma + numero
        i = i + 1 #atualização da variável de controle
    print(f'{soma}')
    return 0
    
if __name__ == "__main__":
    main()
    