'''Faça um programa, em Python 3.x, que receba strings e informe, a partir de uma função, escreva se a string possui letras repetidas, quais são e quantas vezes aparecem na string. . A condição de parada é quando for informada uma string vazia ("").'''

def f_naoExiste(letra, palavra):
    for i in range(len(palavra)):
        if(letra == palavra[i]):
            return False
    return True


def f_repetidas(palavra):
    repetidas = ""
    for i in range(len(palavra)):
        for j in range(i+1,len(palavra)):
            if(palavra[i] == palavra[j]):
                if(f_naoExiste(palavra[i],repetidas)):
                    repetidas += palavra[i]
    return repetidas


def f_contaRepetidas(repetidas,palavra):
    for i in range(len(repetidas)):
        cont = 0
        for j in range(len(palavra)):
            if(repetidas[i] == palavra[j]):
                cont += 1
        print(f'{repetidas[i]}={cont}')


def main():
    #declaração de variáveis
    palavra = str("")
    #entrada de dados e processamento
    palavra = input().upper()
    while(palavra != ""):
        print(palavra)
        repetidas = f_repetidas(palavra)
        if(repetidas != ""):
            f_contaRepetidas(repetidas,palavra)
        else:
            print("NÃO EXISTEM LETRAS REPETIDAS")
        palavra = input().upper()
    return 0
    
if __name__ == "__main__":
    main()