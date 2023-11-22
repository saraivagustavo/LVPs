'''Faça um programa em Python3, DE FORMA MODULAR (DEFININDO E USANDO SUAS PRÓPRIAS FUNÇÕES) EM ARQUIVO EXTERNO para resolver o seguinte problema:
a) Definir uma função em Python 3 que calcule o valor do máximo divisor comum (mdc) entre três números inteiros positivos. Esta função recebe como parâmetro três números inteiros positivos e retorna o valor do mdc calculado. 
b) Faça um programa principal que leia 4 conjuntos com 3 números inteiros positivos. Para cada conjunto de três números lidos, imprima os números lidos na ordem em que foram lidos e o valor do mdc calculado. A saída deste programa deverá ser EXATAMENTE conforme o modelo apresentado nos casos de teste abaixo.
c) Invocar o programa principal.'''

def f_menor(a,b,c):
    if(a < b and a < c):
        return a
    elif(b < c):
        return b
    else:
        return c
        
def f_mdc(a,b,c):
    divisor = f_menor(a,b,c)
    while(divisor > 0):
        if(a % divisor == 0 and b % divisor == 0 and c % divisor == 0):
            return divisor
        divisor -= 1

def main():
    #declaração de variáveis
    numero1 = int(0)
    numero2 = int(0)
    numero3 = int(0)
    resultado_mdc = int(0)
    
    #invocacar a função
    menor = f_menor(numero1,numero2,numero3)
    
    #processamento e saída de dados
    for i in range(4):
        #entrada de dados
        numero1 = int(input())
        numero2 = int(input())
        numero3 = int(input())
        resultado_mdc = f_mdc(numero1, numero2, numero3)
        print(f"MDC({numero1}, {numero2}, {numero3}) = {resultado_mdc}")
    return 0
    
if __name__ == "__main__":
    main()