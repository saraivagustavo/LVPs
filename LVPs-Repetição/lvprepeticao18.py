'''Fazer um programa que calcule e escreva o valor de S:
S = (37 x 38)/1 + (36 x 37)/2 + (35 x 36)/3 + ... + (1 x 2)/37'''

def main():
    #declaração de variáveis
    s = float(0.0)
    i = int(0)
    
    #inicialização de variáveis
    s = 0 #variável acumuladora
    
    #processamento
    for i in range(37, 0, -1):
        s += (i * (i + 1)) / (38 - i)
    
    #saída de dados
    print(f'O valor de S é: {s}')
    return 0
    
if __name__ == "__main__":
    main()
