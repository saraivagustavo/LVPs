'''Faça um programa que recebe dois pares de coordenadas e calcule a distância entre os pontos. '''

def main():
    #declaração de variáveis
    x1 = int (0)
    x2 = int (0)
    y1 = int (0)
    y2 = int (0)
    coordenadaA = int(0)
    coordenadaB = int(0)
    distancia = int(0)

    #entrada de dados
    x1 = int(input("Coordenada de x1: "))
    y1 = int(input("Coordenada de y1: "))
    x2 = int(input("Coordenada de x2: "))
    y2 = int(input("Coordenada de y2: "))
    
    #processamento
    coordenadaA = (x2 - x1)
    coordenadaB = (y2 - y1)
    distancia = ((coordenadaA ** 2) + (coordenadaB ** 2)) ** (1/2)
    
    #saída de dados
    print (f'Distância entre as coordenadas = {distancia}')
    return 0

if __name__ == "__main__":
    main()