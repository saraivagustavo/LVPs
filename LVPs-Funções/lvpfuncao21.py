'''Faça um programa, em Python 3.x, que receba strings e informe, a partir de uma função, escreva uma nova STRING SEM as VOGAIS. Apresente a nova string. A condição de parada é quando for informada uma string vazia ("").'''

def f_removevogal(string):
    novo = ""
    for i in range(len(string)):
        if(string[i] != 'A' and string[i] != 'E' and string[i] != 'I' and string[i] != 'O' and string[i] != 'U'):
            novo += string[i]
    return novo
    
def main():
    #declaração de variáveis
    string = str("")
    #entrada de dados
    string = input().upper()
    #processamento e saída de dados
    while(string != ""):
        print(f'{f_removevogal(string)}')
        string = input().upper()
    return 0
    
if __name__ == "__main__":
    main()