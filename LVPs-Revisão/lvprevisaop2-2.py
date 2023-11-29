'''Faça um programa em Python3 que leia o resultado uma rodada da Copa do Mundo. O programa deve ler o nome do primeiro time e o nome do segundo time, em seguida a quantidade de gols primeiro time e a do segundo time. A condição de parada será informar o nome do primeiro time como string vazia (“”). Após a entrada de dados da partida o programa deverá imprimir o nome do time vencedor, ou imprimir que houve empate, ou imprimir que a quantidade de gols é inválida. Ao final da entrada de dados de todas as partidas da rodada o programa deve informar:
a) A média de gols da rodada
b) O time que fez mais gols em uma mesma partida da rodada
c) A quantidade de gols da partida em que houve o menor número de gols na rodada'''

def main():
    #declaração de variáveis
    time1 = str("")
    time2 = str("")
    gols_time1 = int(0)
    gols_time2 = int(0)
    resultado = str("")
    soma = int(0)
    soma_gols = int(0)
    cont_jogos = int(0)
    media_gols = float(0.0)
    mais_gols = int(0)
    time_mais_gols = str("")
    menor_numero_gols = int(0)
    #inicialização de variáveis acumuladoras
    soma = 0
    soma_gols = 0
    cont_jogos = 0
    #entrada de dados e processamento
    time1 = input() #inicialização da variável de controle
    while(time1 != ""):
        time2 = input()
        gols_time1 = int(input())
        gols_time2 = int(input())
        if(gols_time1 > gols_time2):
            resultado = time1
        elif(gols_time2 > gols_time1):
            resultado = time2
        else:
            resultado = "Empate"
        print(f'{time1} x {time2}')
        if(gols_time1 != gols_time2):
            print(f'Vencedor: {resultado}')
        else:
            print(f'{resultado}')
        soma = gols_time1 + gols_time2
        soma_gols += soma
        #verificar qual time que fez mais gols
        if(cont_jogos == 0):
            if(gols_time1 > gols_time2):
                mais_gols = gols_time1
                time_mais_gols = time1
            else:
                mais_gols = gols_time2
                time_mais_gols = gols_time2
        else:
            if(gols_time1 > gols_time2) and (gols_time1 > mais_gols):
                mais_gols = gols_time1
                time_mais_gols = time1
            elif(gols_time2 > mais_gols):
                mais_gols = gols_time2
                time_mais_gols = time2
            #verificar o menor número de gols feitos em uma partida
            if(cont_jogos == 0):
                menor_numero_gols = soma
            elif(soma < menor_numero_gols):
                menor_numero_gols = soma
        cont_jogos += 1
        time1 = input() #atualização da variável de controle
    media_gols = soma_gols / cont_jogos
    print(f'Média de Gols: {media_gols:.2f} por jogo')
    print(f'Time que fez mais gols em um jogo: {time_mais_gols}')
    print(f'Menor número de gols em uma partida: {menor_numero_gols}')
    return 0
    
if __name__ == "__main__":
    main()