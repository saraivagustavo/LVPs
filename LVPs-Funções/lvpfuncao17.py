'''Faça um programa em linguagem Python que lê um número n digitado pelo usuário(esse número vai ser a quantidade de termos) e imprime os n primeiros números da sequência de Fibonacci.'''

def f_fibonacci(n):
    #declaração de variáveis
    a = int(0)
    b = int(0)
    #inicialização das variáveis
    a = 0
    b = 1
    #processamento
    for i in range(n):
        a, b = b, a + b
        print(a)

def main():
    #declaração de variáveis
    n = int(0)
    #entrada de dados
    n = int(input())
    #saída de dados
    f_fibonacci(n)
    return 0

if __name__ == "__main__":
    main()