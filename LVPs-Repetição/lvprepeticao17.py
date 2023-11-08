'''Fazer um programa que calcule e escreva o valor de S:
S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50'''

def main():
    #declaração de variáveis
    s = float(0.0)
    denominador = int(0)
    numerador = int(0)
    
    #inicialização de variáveis
    s = 0 #variável acumuladora
    denominador = 1
    
    #processamento
    for numerador in range(1, 100, 2):
        s += numerador / denominador
        denominador += 1
    
    #saída de dados
    print(f'O valor de S é: {s}')
    return 0
    
if __name__ == "__main__":
    main()
