'''Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas e, OBRIGATORIAMENTE, **comando de repetição**. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.'''

def main():
    #declaração de variáveis
    nome = str("")
    invertido = str("")
    
    #entrada de dados
    nome = input().upper()
    
    #processamento
    for i in nome:
        invertido = nome[-1::-1]
        
    #saída de dados
    print(f'{invertido}') 
    return 0

if __name__ == "__main__":
    main()