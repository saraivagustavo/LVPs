'''Faça um programa que receba um número inteiro de 3 dígitos e apresente esse número ao contrário. Ex: 123 >> 321  ;  981 >> 189'''

def main():
    #declaração de variáveis
    numero = int(0)
    centena = int(0)
    dezena = int(0)
    unidade = int(0)
    parte = int(0)
    
    #entrada de dados
    numero = int(input("Digite o número: "))
    
    #processamento
    centena = numero // 100
    parte = numero // 10
    dezena = parte % 10
    unidade = numero % 10
    invertido = unidade * 100 + dezena * 10 + centena
    
    #saída de dados
    print(f' Número invertido = {invertido}')
    return 0
    
if __name__ == "__main__":
    main()