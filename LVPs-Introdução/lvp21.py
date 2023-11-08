'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

1. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 2 situações:
2. comprar apenas latas de 18 litros;
3. comprar apenas galões de 3,6 litros;
Para introdução ao conceito de funções, apresentamos a função math

bibliotecas externas precisam ser importadas. Na primeira linha do programa insira a linha:
import math
math possui diversos métodos, entre eles:

Método math.floor(): Arredonda para baixo, até o inteiro mais próximo
Método math.ceil(): Arredonda para cima, até o inteiro mais próximo

Exemplo de Utilização:
math.floor(45.86)
# Retorna: 45
math.ceil(56.45)
# Retorna: 57
Com isso, arredonde o número de latas para cima (considere, então, apenas latas cheias)'''

import math

def main():
    #declaração de variáveis
    area = float(0.0)
    
    #entrada de dados
    area = float(input())
    
    #processamento
    litros = area / 6
    latas = math.ceil(litros / 18)
    galoes = math.ceil(litros / 3.6)
    valor_latas = latas * 80
    valor_galoes = galoes * 25
    
    #saída de dados
    print(f'Você utilizará {latas} de 18L. Valor = {valor_latas:.2f}')
    print(f'Você utilizará {galoes} de 3.6L. Valor = {valor_galoes:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()