'''Um número de Armstrong é um número de N dígitos onde a soma de cada dígito, elevado a N, é igual ao próprio número.
Veja um exemplo com um número de 3 dígitos em base 10:
153 = 1**3 + 5**3 + 3**3 =  1 + 125 + 27 = 153
Escreva um programa que imprima todos os números de Armstrong em base 10 que tenham até 6 dígitos, começando por 1.
Resolva esse exercício utilizando, apenas DIV e MOD.'''

def f_tamanho(n):
    tamanho = 0
    while(n > 0):
        n = n // 10
        tamanho += 1
    return tamanho
    
def f_armstrong(n):
    soma = 0
    comparar = n
    potencia =  f_tamanho(n)
    while(n > 0):
        resto = n % 10
        soma += resto ** potencia
        n = n // 10
    return soma == comparar
        
def main():
    for i in range(1,1000000):
        if(f_armstrong(i)):
            print(i)
    return 0

if __name__ == "__main__":
    main()