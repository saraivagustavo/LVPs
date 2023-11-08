'''Tendo como dados de entrada os sexo, o peso e a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

- para homens: (72.7 * h) - 58
- para mulheres: (62.1 * h) - 44.7

E que calcule seu IMC - Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC o peso dividido pelo quadrado da altura

A condição do indivíduo segue a classificação da tabela abaixo:

IMC	Classificação
Abaixo de 17	MUITO ABAIXO DO PESO
Entre 17 e 18,49	ABAIXO DO PESO
Entre 18,50 e 24,99	PESO NORMAL
Entre 25 e 29,99	ACIMA DO PESO
Entre 30 e 34,99	OBESIDADE I
Maior que 34,99	OBESIDADE II (SEVERA)
Elabore um programa que apresente o peso ideal de uma pessoa e sua classificação de IMC'''

def main():
    #declaração de variáveis
    sexo = str("")
    peso = float(0.0)
    altura = float(0.0)
    peso_ideal = float(0.0)
    imc = float(0.0)
    
    #entrada de dados
    sexo = input().upper()
    peso = float(input())
    altura = float(input())
    
    #processamento
    if(sexo == 'M'):
        peso_ideal = (72.7 * altura) - 58
    else:
        peso_ideal = (62.1 * altura) - 44.7
        
    imc = peso / (altura ** 2)
    
    #saída de dados 
    print(f'PESO IDEAL: {peso_ideal:.2f}')
    print(f'IMC: {imc:.2f}')
    if(imc < 17):
        print('MUITO ABAIXO DO PESO')
    elif(imc < 18.5):
        print('ABAIXO DO PESO')
    elif(imc < 25):
        print('PESO NORMAL')
    elif(imc < 30):
        print('ACIMA DO PESO')
    elif(imc < 35):
        print('OBESIDADE I')
    else:
        print('OBESIDADE II (SEVERA)')
    
    return 0
    
if __name__ == "__main__":
    main()
