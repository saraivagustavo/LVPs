'''Escreva um programa para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo.'''

def main():
    #declaração de variáveis
    base = int(0)
    altura = int(0)
    
    #entrada de dados
    base = int(input("Digite o valor inteiro da base: "))
    altura = int(input("Digite o valor inteiro da altura: "))
    
    #processamento 
    area = base * altura
    
    #saída de dados
    print(f'Área = {area}')
    return 0
    
if __name__ == "__main__":
    main()