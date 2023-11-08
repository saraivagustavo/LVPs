'''Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média escrever a mensagem 'NÃO EFETUAR COMPRA', senão escrever a mensagem 'EFETUAR COMPRA'.'''

def main():
    #declaração de variáveis
    qntd_atual = int(0)
    qntd_maxima = int(0)
    qntd_minima = int(0)
    qntd_media = int(0)
    
    #entrada de dados
    qntd_atual = int(input())
    qntd_maxima = int(input())
    qntd_minima = int(input())
    
    #processamento
    qnts_media = (qntd_maxima + qntd_minima) / 2
    
    #saída de dados
    if(qntd_atual >= qntd_media):
        print('NÃO EFETUAR COMPRA')
    else:
        print('EFETUAR COMPRA')
        
    return 0
    
if __name__ == "__main__":
    main()