'''Faça um programa em Python3, DE FORMA MODULAR (DEFININDO E USANDO SUAS PRÓPRIAS FUNÇÕES) EM ARQUIVO EXTERNO para resolver o seguinte problema:
a) Definir uma função em Python 3 que calcule o valor do máximo divisor comum (mdc) entre três números inteiros positivos. Esta função recebe como parâmetro três números inteiros positivos e retorna o valor do mdc calculado. 
b) Faça um programa principal que leia 4 conjuntos com 3 números inteiros positivos. Para cada conjunto de três números lidos, imprima os números lidos na ordem em que foram lidos e o valor do mdc calculado. A saída deste programa deverá ser EXATAMENTE conforme o modelo apresentado nos casos de teste abaixo.
c) Invocar o programa principal.'''

from mdc import f_mdc_tres

def main():
    #declaração de variáveis
    numero1 = int(0)
    numero2 = int(0)
    numero3 = int(0)
    resultado_mdc = int(0)
    
    #processamento e saída de dados
    for i in range(4):
        #entrada de dados
        numero1 = int(input())
        numero2 = int(input())
        numero3 = int(input())
        resultado_mdc = f_mdc_tres(numero1, numero2, numero3)
        print(f"MDC({numero1}, {numero2}, {numero3}) = {resultado_mdc}")
    return 0
    
if __name__ == "__main__":
    main()