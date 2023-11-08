'''Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.'''

def main():
    #declaração de variáveis
    salario_fixo = float(0.0)
    total_vendas = float(0.0)
    
    #entrada de dados
    salario_fixo = float(input())
    total_vendas = float(input())
    
    #saída de dados
    if(total_vendas <=1500):
        print(salario_fixo + (total_vendas * (3 / 100)))
    else:
        print(salario_fixo + ((total_vendas - 1500) * (3 / 100)) + ((total_vendas - 1500) * (5 / 100)))
        
    return 0
    
if __name__ == "__main__":
    main()
    