'''Considere um programa que contenha um menu de seis opções (de 1 a 6). Faça uma validação de entrada, em Python 3.x, que valide o input do usuário da seguinte forma: caso o usuário digite uma opção fora desses valores, exiba a mensagem "OPÇÃO INVÁLIDA. DIGITE UM VALOR DE 1 A 6", e caso ele informe uma opção dentro do esperado, apresenta  a mensagem "OPÇÃO VÁLIDA".'''

def main():
    #declaração de variáveis
    opcao = int(0)
    
    #entrada de dados
    opcao = int(input())
    
    #processamento e saída de dados
    while(opcao < 1 or opcao > 6):
        print(f"OPÇÃO INVÁLIDA. DIGITE UM VALOR DE 1 A 6")
        opcao = int(input())
    if(opcao >= 1 and opcao <= 6):
        print(f"OPÇÃO VÁLIDA")
    return 0
    
if __name__ == "__main__":
    main()