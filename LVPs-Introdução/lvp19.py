'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

def main():
    #declaração de variáveis 
    salario = float(0.0)
    horas = int (0)
    salario_bruto = float(0.0)
    imposto_renda = float(0.0)
    inss = float(0.0)
    sindicato = float(0.0)
    salario_liquido = float(0.0)
    desconto = float(0.0)

    #entrada de dados
    salario = float(input("Reais por hora: "))
    horas = int(input("Horas trabalhadas: "))

    #processamento
    salario_bruto = salario * horas
    imposto_renda = salario_bruto * (11 / 100)
    inss = salario_bruto * (8 / 100)
    sindicato = salario_bruto * (5 / 100)
    desconto = imposto_renda + inss + sindicato
    salario_liquido = salario_bruto - desconto

    #saída de dados
    print(f'+ Salário Bruto : R$ {salario_bruto:.2f}')
    print(f'- IR (11%) : R$ {imposto_renda:.2f}')
    print(f'- INSS (8%) : R$ {inss:.2f}')
    print(f'- Sindicato (5%) : R$ {sindicato:.2f}')
    print(f'= Salário Líquido : R$ {salario_liquido:.2f}')
    return 0

if __name__ == "__main__":
    main()