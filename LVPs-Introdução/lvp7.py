'''Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.'''

def main():
    #declaração de variáveis
    salario = int(0)
    reajuste = int(0)
    
    #entrada de dados
    salario = int(input("Digite o salário: "))
    reajuste = int(input("Digite o percentual de reajuste: "))
    
    #processamento
    novosalario = salario * (reajuste / 100) + salario
    
    #saída de dados
    print(f'"Novo valor do salário do salário: {novosalario}')
    return 0
    
if __name__ == "__main__":
    main()