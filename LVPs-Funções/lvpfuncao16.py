'''Um número de Armstrong é um número de N dígitos onde a soma de cada dígito, elevado a N, é igual ao próprio número.
Veja um exemplo com um número de 3 dígitos em base 10:
153 = 13 + 53 + 33 =  1 + 125 + 27 = 153
Escreva um programa que imprima todos os números de Armstrong em base 10 que tenham até 6 dígitos, começando por 1.
Resolva esse exercício utilizando STRING.'''

def main():
    #declaração de variáveis
    n = int(0)
    soma = int(0)
    #processamento e saída de dados
    for i in range(1, 1000000):
        soma = 0
        n = str(i)
        for j in range(len(n)):
            soma += int(n[j]) ** len(n)
        if(i == soma):
            print(soma)

if __name__ == "__main__":
    main()
    
#----------------------#

def f_checa_numero(x):
    soma = 0
    for i in range (len(x)):
        soma += int (x[i])**len(x)
    return soma
def main():
    s = 1 
    x = str()
    while len(x) <= 6:
        x = str(s)
        if str(f_checa_numero(x)) == x:
            print(x)
        s += 1
    return 0
if __name__ == "__main__":
    main()