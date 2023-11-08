'''Fazer um programa que calcule e escreva o valor de S:
S = 1/1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 ... - 10/100'''

def main():
    #declaração de variáveis
    s = float(0.0)
    i = int(0)
    
    #inicialização das variáveis
    s = 0 #variável acumuladora
    
    #processamento
    for i in range(1, 11):
        if(i % 2 == 0):
            s -= i / (i * i)
        else:
            s += i / (i * i)
    
    #saída de dados
    print(f'O valor de S é: {s}')
    return 0
    
if __name__ == "__main__":
    main()