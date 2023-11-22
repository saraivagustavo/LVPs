'''Faça um programa que recebe n números inteiros maiores ou iguais a zero. Considere que a entrada de encerra quando um número menor que zero for informado pelo usuário.
 - Faça uma função externa que receba um número inteiro maior ou igual a zero na base 10 e retorne um número inteiro maior ou igual a zero que representa, na base 2 (binário), o número na base 10 fornecido como entrada para esta função.  
 - Faça uma função externa que receba um número inteiro maior ou igual a zero na base 10 e retorne um número inteiro maior ou igual a zero que representa, na base 16 (hexadecimal), o número na base 10 fornecido como  entrada para esta função.'''

def f_decimal2binario(n): #transforma a variável "numero" da função main na variável "n"
    #declaração de variáveis
    b = str("")
    #inicialização da variavel acumuladora
    b = ""
    while(n > 0):
        resto = n % 2
        b = str(resto) + b
        n = n // 2
    return b

def f_decimal2hexadec(n): #transforma a variável "numero" da função main na variável "n"
    #declaração de variáveis
    h = str("")
    #inicialização da variavel acumuladora
    h = ""
    while(n > 0):
        resto = n % 16
        if (resto < 10):
            h = str(resto) + h
        else:
            h = f_letrahexadec(resto) + h
        n = n // 16
    return h

#solução elegante
def f_letrahexadec(x):
    hexadec = 'ABCDEF'
    return hexadec[x-10]

def main():
    numero = int(input())
    binario = f_decimal2binario(numero) #envia a variável "numero" para a função f_decimal2binario
    hexadec = f_decimal2hexadec(numero) #envia a variável "numero" para a função f_decimal2hexadec
    print(f'DEC={numero} BIN={binario} HEX={hexadec}')
    return 0

if __name__ == "__main__":
    main()