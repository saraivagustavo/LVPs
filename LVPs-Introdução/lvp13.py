'''Faça um programa que receba a idade de uma pessoa, em dias, e apresente a idade dessa pessoa em anos, meses e dias. Considere um ano com 365 dias e um MÊS com 30 dias.'''

def main():
    #declaração de variáveis
    diastotais = int(0)
    anos = int(0)
    meses = int(0)
    dias = int(0)
    
    #entrada de dados
    diastotais = int(input("Digite os dias totais: "))
    
    #processamento 
    anos = diastotais // 365
    meses = (diastotais % 365) // 30
    dias = (diastotais % 365) % 30
    
    #saída de dados
    print(f'{anos} anos,{meses} meses,{dias} dias')
    return 0
if __name__ == "__main__":
    main()