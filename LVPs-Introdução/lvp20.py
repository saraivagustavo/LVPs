'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em segundos).'''

def main():
    #declaração de variáveis
    tamanho = float(0.0)
    velocidade = float(0.0)
    tempo = float(0.0)
    
    #entrada de dados
    tamanho = float(input())
    velocidade = float(input())
    
    #processamento de dados
    tempo = tamanho / (velocidade / 8)
    
    #saída de dados
    print(f'{tempo:.2f} segundos')
    return 0

if __name__ == "__main__":
    main()