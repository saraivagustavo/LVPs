'''Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos), em formato 24h. Calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.'''

def main():
    #declaração de variáveis
    hora_inicio = int(0)
    hora_fim = int(0)
    14
    #entrada de dados
    hora_inicio = int(input())
    hora_fim = int(input())
    
    #saída de dados
    if hora_fim < hora_inicio:
        print(24 - hora_inicio + hora_fim)
    else:
        print(hora_fim - hora_inicio)
        
    if(hora_inicio == hora_fim):
        print(24)
        
    return 0
    
if __name__ == "__main__":
    main()
