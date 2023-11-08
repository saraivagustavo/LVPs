'''Faça um programa que solicite o nome do usuário e imprima-o na vertical.'''

def main():
    #declaração de variáveis
    nome = str("")
    
    #entrada de dados
    nome = input().upper()
    
    #processamento e saída de dados
    for i in nome:
        print(i)
    return 0

if __name__ == "__main__":
    main()
  