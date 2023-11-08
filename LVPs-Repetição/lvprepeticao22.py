'''Um jogo de videogame gera um relatório após processar os dados de um campeonato. Neste campeonato, os jogadores participam de 10 fases, onde os pontos são contabilizados por tipos de erros e tipos de acertos para cada fase. Os acertos são caracterizados pelas strings: A1, A2 e A3. Já os erros são  caracterizados pelas strings: E1, E2, E3.
 A1: soma 5 pontos
 A2: soma 7 pontos
 A3: soma 10 pontos
 E1: subtrai 2 pontos, se tiver pontos > 0
 E2: subtrai 5 pontos, se tiver pontos > 0
 E3: zera a pontuação
Os dados são fornecidos nesta ordem:
 1. Nickname do jogador
 2. Tipo de erro/acerto para cada uma das 10 fases.
Considere que os dados encerram quando um nickname igual a string vazia for fornecido para o
jogador.
Seu programa deverá calcular, para cada jogador, a pontuação ao final das 10 fases, sendo que toda
vez que a pontuação se tornar negativa deverá ser zerada. Imprima o nome do jogador e sua
pontuação final.
Ao final do campeonato imprima:
 - A média de pontos do campeonato;
 - O nome e a pontuação do jogador com maior pontuação;'''

def main():
    #declaração de variáveis
    nickname = str("")
    soma = int(0)
    ponto = str("")
    soma_pontos = int(0)
    cont = int(0)
    media = float(0.0)
    
    #inicialização das variáveis
    soma_pontos = 0
    cont = 0
    
    #entrada de dados
    nickname = input("Digite o nickname: ") #variável de controle, o nickname é como se fosse uma "flag"
    while(nickname != ""):
        soma = 0 #zera a variável soma pra cada jogador
        for i in range(10):
            ponto = input("Digite o tipo de ponto feito: ")
            if(ponto == "A1"):
                soma += 5
            elif(ponto == "A2"):
                soma += 7
            elif(ponto == "A3"):
                soma += 10  
            elif(ponto == "E1"):
                soma -= 2
            elif(ponto == "E2"):
                soma -= 5
            elif(ponto == "E3"):
                soma = 0
                
            if(soma < 0):
                soma = 0
        
        #imprimir cada jogador com sua pontuação final        
        print(f'{nickname} {soma} pontos')
        
        #variável acumuladora para realizar média dos pontos
        soma_pontos += soma
        
        #verifica qual o jogador com mais pontos
        if(cont == 0):
            maior_nickname = nickname
            maior_soma = soma
        elif(soma > maior_soma):
            maior_nickname = nickname
            maior_soma = soma
        cont += 1
        nickname = input("Digite outro nickname: ") #atualização da variável de controle
        media = soma_pontos/cont
    
    #saída de dados
    print(f'Média de pontos = {media:.2f} por jogo')
    print(f'Vencedor {maior_nickname} com {maior_soma} pontos')
    return 0
    
if __name__ == "__main__":
    main()
        