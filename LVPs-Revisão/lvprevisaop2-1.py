'''Faça um programa, em Python 3.x, que solucione o seguinte somatório:
S =  - (1 + 1)/2 + (2 + 4)/4 - (3 + 9)/6 + (4 + 16)/8 ..... - (9 + 81)/18 + (10 + 100)/20'''

def main():
    #declaração de variáveis
    s = float(0.0)
    numero1 = int(0)
    numero2 = int(0)
    numerador = int(0)
    denominador = int(0)
    #inicialização das variáveis
    s = 0
    #processamento
    for numero1 in range(1, 11):
        numero2 = numero1 ** 2
        numerador = numero1 + numero2
        denominador = numero1 * 2
        if(numero1 % 2 == 0):
            s += numerador / denominador
        else:
            s -= numerador / denominador
    #saída de dados
    print(f'Resultado: {s}')
    return 0
    
if __name__ == "__main__":
    main()