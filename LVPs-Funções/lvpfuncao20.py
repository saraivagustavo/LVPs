'''Faça um programa, em Python 3.x, que receba strings e informe, a partir de uma função, qual a menor letra do texto (considerando A a menor letra e Z a maior). A condição de parada é quando for informada uma string vazia ("").'''

def f_menor_letra(palavra):
    menor = palavra[0]
    for letra in palavra:
        if(letra < menor):
            menor = letra
    return menor

def main():
    #declaração de variáveis
    palavra = str("")
    #entrada de dados
    palavra = input().upper()
    while(palavra != ""):
        letra_menor = f_menor_letra(palavra)
        print(f"{letra_menor}")
        palavra = input().upper()
    return 0
    
if __name__ == "__main__":
    main()