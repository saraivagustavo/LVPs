'''Leia o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu). Considere o ano atual como 2021 e a idade mínima, para votar, 16 anos.'''

def main():
    #declaração de variáveis
    ano = int(0)
    idade_minima = int(0)
    
    #entrada de dados 
    ano = int(input())
    
    #processamento
    idade_minima = 2021 - ano
    
    #saída de dados
    if(idade_minima >= 16):
        print('PODE VOTAR')
    else:
        print('NÃO PODE VOTAR')
    return 0
    
if __name__ == "__main__":
    main()
    