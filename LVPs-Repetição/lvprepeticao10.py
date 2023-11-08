'''Faça um algoritmo que leia 5 valores e escreva no final a soma dos valores positivos e a média dos negativos. '''

def main():
    # Declaração de variáveis
    soma_positivos = 0 
    soma_negativos = 0 
    media_negativos = 0 
    i_negativos = 0 #inicialização da variável de controle dos números NEGATIVOS
    numero = int(0)

    # Entrada de dados
    i = 0  #inicialização da variável de controle dos números POSITIVOS
    while(i < 5):
        numero = int(input("Digite um número: "))
        if(numero > 0):
            soma_positivos = soma_positivos + numero
        elif(numero < 0):
            i_negativos = i_negativos + 1 #atualização da variável de controle dos números NEGATIVOS
            soma_negativos = soma_negativos + numero
        i = i + 1  #atualização da variável de controle dos números POSITIVOS

    if(i_negativos > 0):
        media_negativos = soma_negativos / i_negativos  
    else:
        media_negativos = 0

    print(f'Soma dos positivos: {soma_positivos}')
    print(f'Média dos negativos: {media_negativos}')

if __name__ == "__main__":
    main()
