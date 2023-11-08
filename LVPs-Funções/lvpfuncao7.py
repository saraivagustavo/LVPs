'''Dado o exemplo, faça um programa que calcule a aproximação do quadrado de diversos números INTEIROS pelo método de Newton, utilizando funções em um arquivo externo. Utilize uma função para encontrar o quadrado perfeito mais próximo e outra função para calcular a raiz. A condição de parada será quando um número negativo for informado.'''

def f_maisPróximo(x,a):
 if (a - x**2 < (x+1)**2 - a):
    return x
 else:
    return x + 1

def f_procuraRaizProx(a):
    n = 1
    while(n**2 < a):
        n = n + 1
    n = f_maisPróximo(n-1,a)
    return n**2

def f_calculaRaizNewton(a):
    x2 = f_procuraRaizProx(a)
    x = x2**(1/2)
    raiz = (a+x2)/(2*x)
    return raiz

def main():
    a = int(input("Raiz desejada: "))
    raiz = f_calculaRaizNewton(a)
    print(f'{raiz:.6f}')
    return 0

if __name__ == "__main__":
    main()