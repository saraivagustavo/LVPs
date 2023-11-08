'''Efetuar a leitura de três valores (variáveis A, B e C) e efetuar o cálculo da equação completa de segundo grau, apresentando as duas raízes, se para os valores informados for possível efetuar o referido cálculo. Lembre-se de que a variável A deve ser diferente de zero.'''

#importar biblioteca matemática
import math

def main():
    #declaração de variáveis
    valora = float(0.0)
    valorb = float(0.0)
    valorc = float(0.0)
    
    #entrada de dados
    valora = float(input())
    valorb = float(input())
    valorc = float(input())
    
    #verificar se é equação do 2 grau
    if(valora == 0):
        print('Não possui raiz')
    #definir o valor de delta
    delta = (valorb ** 2) - (4 * valora * valorc)
    if(delta < 0):
        print('Não possui raiz')
    #definir o valor das raízes
    if(valora != 0 and delta >= 0):
        x1 = round(((-valorb) + (delta ** 0.5)) / (2 * valora), 2)
        x2 = round(((-valorb) - (delta ** 0.5)) / (2 * valora), 2)
    #exibir o resultado
    print(f'{x1} {x2}')
    return 0
        
if __name__ == "__main__":
    main()