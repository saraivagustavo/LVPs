'''Faça um programa que leia o raio de uma circunferência, calcule e apresente a área da mesma. Considere o valor de pi como 3.14159'''

def main():
    #declaração de variáveis
    raio = float(0.0)
    pi = 3.14159
    area = float(0.0)
    
    #entrada de dados
    raio = float(input("Digite o raio: "))
    
    #processamento
    area = pi * (raio ** 2)
    
    #saída de dados
    print(f'Área = {area}')
    return 0
    
if __name__ == "__main__":
    main()
