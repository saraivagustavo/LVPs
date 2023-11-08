'''Escreva um programa para ler um valor INTEIRO (do teclado) e escrever (na tela) o seu antecessor.'''

def main():
    #declaração de variáveis
    a = int(0)
    
    #entrada de dados
    a = int(input("Digite um valor inteiro: "))
    
    #processamento
    leitura = a - 1
    
    #saída de dados
    print(f'Antecessor = {leitura}')
    return 0
    
if __name__ == "__main__":
    main()