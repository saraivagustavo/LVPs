'''Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.'''

def main():
    #declaração de variáveis
    salario = int(0)
    comissao = int(0)
    
    #entrada de dados
    qntdvendas = int(input("Quantidade de vendas: "))
    totalvendas = int(input("Valor total das vendas: "))
    salario = int(input("Salário fixo: "))
    comissaofixa = int(input("Comissão fixa: "))
    
    #processamento
    vendasefetuadas = totalvendas * (5 /100)
    comissaovendas = qntdvendas * comissaofixa
    salariototal = vendasefetuadas + comissaovendas + salario
    
    #saída de dados
    print(f'Salário total: {salariototal}')
    return 0
    
if __name__ == "__main__":
    main()