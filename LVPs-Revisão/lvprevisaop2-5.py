'''Ler informações sobre um grupo de 25 pessoas e calcular alguns dados estatísticos.
Para cada pessoa do grupo obter o o sexo (“F” para feminino e “M” para o masculino), a altura e o peso. Calcular e escrever:
As letras de A, C e D devem ser efetuadas com utilização de funções externas.
O preenchimento das listas de sexo, altura e peso podem ser preenchidas diretamente na função.
Dica: para testar se funciona, teste com 5 pessoas, para não ter que digitar 75 informações toda vez que testar.
a) A média de peso dos homens
b) A maior peso entre os homens
c) A média de peso do grupo
d) A média de altura entre as mulheres
e) A menor altura entre as mulheres'''

def f_media(soma,cont):
    return soma / cont

def main():
    #declaração de variáveis
    sexo = str("")
    altura = float(0.0)
    peso = float(0.0)
    soma_peso_m = float(0.0)
    maior_peso_m = float(0.0)
    cont_m = int(0)
    soma_peso_geral = float(0.0)
    soma_altura_f = float(0.0)
    menor_altura_f = float(0.0)
    cont_f = int(0)
    primeiroM = True
    primeiroF = True
    #processamento
    for i in range(25):
        #entrada de dados
        sexo = input().upper()
        altura = float(input())
        peso = float(input())
        soma_peso_geral += peso
        if(sexo == "M"):
            cont_m += 1
            soma_peso_m += peso
            if(primeiroM): #a primeira pessoa é a com maior peso
                maior_peso_m = peso
                primeiroM = False
            elif(peso > maior_peso_m): #se algum peso for maior que o primeiro registrado, se torna o maior
                maior_peso_m = peso
        else:
            soma_altura_f += altura
            cont_f += 1
            if(primeiroF): #a primeira pessoa é a com menor altura
                menor_altura_f = altura
                primeiroF = False
            elif(altura < menor_altura_f):  #se alguma altura for maior que a primeira registrada, se torna a menor
                menor_altura_f = altura
    print(f'{f_media(soma_peso_m,cont_m):.2f}')
    print(f'{maior_peso_m:.2f}')
    print(f'{f_media(soma_peso_geral,25):.2f}')
    print(f'{f_media(soma_altura_f,cont_f):.2f}')
    print(f'{menor_altura_f:.2f}')
    return 0
        
if __name__ == "__main__":
    main()