'''Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, é um "natural" e você ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número outra vez, quando você tirar esse número, você "ganhou". Apresente o número de jogadas que foram necessárias para você ganhar.
No entanto, você perde, se tirar um 7 antes de tirar este "Ponto" novamente. Apresente o número de jogadas que você fez até perder.'''

from random import randrange

def f_jogarDados():
    return randrange(1,7)
    
def main():
    #declaração de variáveis
    jogada = int(0)
    ponto = int(0)
    
    #entrada de dados
    jogada = int(input())
    print(jogada)
    
    #processamento e saída de dados
    cont = 1
    if(jogada == 7 or jogada == 11):
        print("NATURAL! VOCÊ GANHOU")
        print(f'JOGADAS = {cont}')
    elif(jogada == 2 or jogada == 3 or jogada == 12):
        print("CRAPS! VOCÊ PERDEU")
        print(f'JOGADAS = {cont}')
    else:
        ponto = jogada
        jogada = int(input())
        cont += 1
        while(ponto != jogada and jogada != 7):
            print(jogada)
            jogada = int(input())
            cont += 1
        print(jogada)
        if(jogada == ponto):
            print("VOCÊ GANHOU")
            print(f"JOGADAS = {cont}")
        elif(jogada == 7):
            print("VOCÊ PERDEU")
            print(f"JOGADAS = {cont}") 
    return 0
    
if __name__ == "__main__":
    main()
    