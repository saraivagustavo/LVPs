'''Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em
uma determinada cidade. Para isso, são fornecidos os seguintes dados:
 - preço do kWh consumido;
 - número do consumidor;
 - quantidade de kWh consumidos durante o mês;
 - código do tipo de consumidor (R-residencial, C-comercial, I-industrial).
O número do consumidor igual a zero deve ser usado como flag de parada. 
Fazer um algoritmo que leia os dados descritos acima e calcule:
 a) para cada consumidor, o total a pagar;
 b) o maior consumo verificado;
 c) o menor consumo verificado;
 d) o total do consumo para cada um dos três tipos de consumidores;
 e) a média geral de consumo;
Escreva na saída:
 a) para cada consumidor, o seu número e o total a pagar;
 b) o que foi calculado nos itens b, c, d, e'''

def main():
    #declaração de variáveis
    preco_kwh = float(0.0)
    consumidor = int(0) #variável de controle
    quantidade_kwh = float(0.0)
    tipo = str("")
    total = float(0.0)
    maior = float(0.0)
    menor = float(0.0)
    total_R = float(0.0)
    total_C = float(0.0)
    total_I = float(0.0)
    soma_kwh = float(0.0)
    cont_consumidor = int(0)
    media = float(0.0)
    
    #inicialização das variáveis acumuladoras 
    total_R = 0
    total_C = 0
    total_I = 0
    cont_consumidor = 0
    soma_kwh = 0
    
    #processamento e entrada de dados
    preco_kwh = float(input("Digite o valor do Kwh: "))
    consumidor = int(input("Digite o código do consumidor: ")) #inicialização da variável de controle
    while(consumidor != 0): #condição de parada
        quantidade_kwh = float(input("Consumo: "))
        tipo = input("Digite o tipo de consumidor: ")
        total = preco_kwh * quantidade_kwh
        print(f'{consumidor} {total}') #letra A (precisa printar dentro do looping pra imprimir cada consumidor, fora do looping vai sair 0)
        if(cont_consumidor == 0): #o primeiro consumidor vai ser o maior e menor para usar de parâmetro
            maior = quantidade_kwh
            menor = quantidade_kwh
        elif(quantidade_kwh > maior):
            maior = quantidade_kwh #letra B: achando o maior consumo
        elif(quantidade_kwh < menor):
            menor = quantidade_kwh #letra B: achando o menor cosumo
        #letra D   
        if(tipo.upper() == "R"):
            total_R += quantidade_kwh
        elif(tipo.upper() == "C"): 
            total_C += quantidade_kwh
        elif(tipo.upper() == "I"): 
            total_I += quantidade_kwh
            
        soma_kwh += quantidade_kwh
        cont_consumidor += 1
        consumidor = int(input("Digite o código de outro consumidor: ")) #atualização da variável de controle
    
    media = soma_kwh / cont_consumidor
    print(f'Maior consumo de Kwh: {maior}') #letra B
    print(f'Menor consumo de Kwh: {menor}') #letra C
    print(f'Total de consumo do tipo "R": {total_R}') #letra D
    print(f'Total de consumo do tipo "C":{total_C}') #letra D
    print(f'Total de consumo do tipo "I":{total_I}') #letra D
    print(f'Média de consumo total: {media}') #letra E
    return 0
    
if __name__ =="__main__":
    main()
