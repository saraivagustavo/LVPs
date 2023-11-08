'''Tendo como dados de entrada a altura e o sexo (M ou F) de uma pessoa, calcule e mostre seu peso ideal, utilizando as seguintes fórmulas: - para sexo masculino: peso ideal = (72.7 * altura) - 58 – para sexo feminino: peso ideal = (62.1 * altura) - 44.7'''

def main():
    #declaração de variáveis
    altura = float(0.0)
    sexo = str
    
    #entrada de dados
    sexo = input()
    altura = float(input())
    
    #saída de dados
    if(sexo == 'M'):
        print((72.7 * altura) - 58)
    else:
        print((62.1 * altura) - 44.7)
        
    return 0
    
if __name__ == "__main__":
    main()