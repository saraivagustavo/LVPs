'''Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.'''

def main():
    #declaração de variáveis 
    anos = int(0)
    meses = int(0)
    dias = int(0)
    
    #entrada de dados
    anos = int(input("Digite quantos anos de idade você tem: "))
    meses = int(input("Digite quantos meses de idade você tem: "))
    dias = int(input("Digite quantos dias de idade você tem: "))
    
    #processamento
    diastotais = (anos * 365) + (meses * 30) + dias
    
    #saída de dados
    print(f'Dias totais = {diastotais}')
    return 0
    
if __name__ == "__main__":
    main()