'''Um veículo parte do repouso em movimento retilíneo e acelera com aceleração escalar. Faça um programa, em Python 3.x, que leia a aceleração e o tempo decorrido do movimento desse veículo e calcule a velocidade escalar e a distância percorrida (usando a fórmula de movimento uniformemente variado) por um veículo.'''

def main():
    #declaração de variáveis
    aceleracao = float(0.0)
    tempo = float(0.0)
    velocidade_inicial = 0
    espaco_inicial = 0
    velocidade = float(0.0)
    distancia = float(0.0)
    
    #entrada de dados
    aceleracao = float(input("Digite a aceleração: "))
    tempo = float(input("Digite o tempo: "))
    
    #processamento
    velocidade = velocidade_inicial + aceleracao * tempo
    distancia = espaco_inicial + velocidade_inicial * tempo + (aceleracao * (tempo ** 2)) / 2
    
    #saída de dados
    print(f'{velocidade} m/s e {distancia} m')
    return 0
    
if __name__ == "__main__":
    main()