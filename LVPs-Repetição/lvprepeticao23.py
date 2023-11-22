'''Faça um programa em Python3 que leia o resultado uma rodada de um campeonato de futebol. O programa deve ler o nome do primeiro time e o nome do segundo time, em seguida a quantidade de gols primeiro time e a do segundo time (validação: aceite apenas valores maiores ou iguais a zero, caso ocorram entradas incorretas retorne à entrada dos dados). A condição de parada será informar o nome do primeiro time como string vazia (""). Após a entrada de dados da partida o programa deverá imprimir o nome do time vencedor, ou imprimir que houve empate, ou imprimir que a quantidade de gols é inválida. Ao final da entrada de dados de todas as partidas da rodada o programa deve informar:
 a) A média de gols da rodada
 b) O time que fez mais gols em uma mesma partida da rodada
 c) A quantidade de gols da partida em que houve o menor número de gols na rodada'''

def main():
    #declaração de variáveis
    time1 = str("")
    time2 = str("")
    gols_time1 = int(0)
    gols_time2 = int(0)
    