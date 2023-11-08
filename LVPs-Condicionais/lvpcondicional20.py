'''Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem mais novo com a mulher mais velha.'''

def main():
    #declaração de variáveis
    homem1 = int(0)
    homem2 = int(0)
    mulher1 = int(0)
    mulher2 = int(0)
    
    #entrada de dados
    homem1 = int(input())
    homem2 = int(input())
    mulher1 = int(input())
    mulher2 = int(input())
    
    #processamento de dados
    #descobrir o homem mais velho e mais novo
    if(homem1 > homem2):
        mais_velho = homem1
        mais_novo = homem2
    else:
        mais_velho = homem2
        mais_novo = homem1
    #descobrir a mulher mais  velha e mais nova
    if(mulher1 > mulher2):
        mais_velha = mulher1
        mais_nova = mulher2
    else:
        mais_velha = mulher2
        mais_nova = mulher1
        
    soma_idades = mais_velho + mais_nova
    produto_idades = mais_novo * mais_velha
    
    #saída de dados
    print(f'{soma_idades} {produto_idades}')
    return 0
    
if __name__ == "__main__":
    main()
    