'''Tem-se um conjunto de dados contendo o sexo (masculino, feminino) e a altura de 5 pessoas. Fazer um algoritmo que calcule e escreva:
 - a maior e a menor altura do grupo;
 - a média de altura das mulheres;
 - a quantidade de homens;'''

def main():
    #declaração de variáveis
    sexo = str("")
    altura = float(0.0)
    maior = float(0.0)
    menor = float(0.0)
    soma_altura_f = float(0.0)
    media_altura_f = float(0.0)
    contador_f = int(0)
    contador_m = int(0)
    i = int(0) #variável de controle
    
    #inicialização das variáveis de controle/acumuladoras 
    i = 0
    contador_f = 0
    contador_m = 0
    soma_altura_f = 0
    
    #entrada de dados
    while(i < 5):
        sexo = input("Digite o sexo (f/m): ")
        altura = float(input("Digite a altura: "))
        #coletar a menor e a maior altura do grupo
        if(i == 0):
            maior = altura
            menor = altura
        elif(altura > maior):
            maior = altura
        elif(altura < menor):
            menor = altura
        if(sexo.upper() == "F"):
            soma_altura_f += altura
            contador_f += 1
        else:
            contador_m += 1
        i += 1
    media_altura_f = soma_altura_f / contador_f
    
    print(f'Maior altura: {maior}')
    print(f'Menor altura: {menor}')
    print(f'Média de altura das mulheres: {media_altura_f}')
    print(f'Quantidade de homens: {contador_m}')
    return 0
    
if __name__ == "__main__":
    main()
