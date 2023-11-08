'''Faça um programa que leia 2 strings e informe se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.'''

def main():
    #declaração de variáveis
    string1 = str("")
    string2 = str("")
    
    #entrada de dados
    string1 = input()
    string2 = input()
    
    #processamento e saída de dados
    if(len(string1) == len(string2)):
        print(f'MESMO TAMANHO')
    else:
        print(f'TAMANHO DIFERENTE')
    if(string1 == string2):
        print(f'CONTEÚDO IGUAL')
    else:
        print(f'CONTEÚDO DIFERENTE')
    return 0
    
if __name__ == "__main__":
    main()
