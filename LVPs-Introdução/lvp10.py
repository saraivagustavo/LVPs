'''Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius. Fórmula: c = (f-32)/1.8'''

def main():
    #declaração de variáveis
    fahrenheit = int(0)
    
    #entrada de dados
    fahrenheit = int(input("Temperatura em Fahrenheit: "))
    
    #processamento 
    celsius = (fahrenheit - 32) / (180 / 100)
    
    #saída de dados
    print(f'Temperatura em Celsius: {celsius}°C')
    return 0
    
if __name__ == "__main__":
    main()