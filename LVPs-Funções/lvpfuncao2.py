'''Faça um programa que leia três número e, a partir de uma função, informe o resultado da soma, dos mesmos.'''

def f_soma(x,y,z):
    resultado = x + y + z
    return resultado

def main():
    #declaração de variáveis
    a = int(0)
    b = int(0)
    c = int(0)
    soma = int(0)
    
    #entrada de dados
    a = int(input('Valor de A: '))
    b = int(input('Valor de B: '))
    c = int(input('Valor de C: '))
    
    #invocação da função
    soma = f_soma(a,b,c)
    
    #saída de dados
    print(f'Soma: {soma}')
    return 0
    
if __name__ == "__main__":
    main()