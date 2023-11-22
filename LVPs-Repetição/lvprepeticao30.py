'''Faça um programa que solicite que o usuário digite um sexo (M ou F). Na entrada altere esse valor para maiúsculo. Faça uma validação de entrada, em Python 3.x, que valide o input do usuário da seguinte forma: caso o usuário digite um sexo válido, exiba a mensagem "SEXO VÁLIDO", caso o usuário digite um sexo inválido a mensagem "SEXO INVÁLIDO, DIGITE F OU M" deverá ser exibida'''

def main():
    #declaração de variáveis
    sexo = str("")
    
    #entrada de dados
    sexo = input().upper()
    
    #processamento e saída de dados
    while(sexo != "F" and sexo != "M"):
        print(f"SEXO INVÁLIDO, DIGITE F OU M")
        sexo = input().upper()
    if(sexo == "F" or sexo == "M"):
        print(f"SEXO VÁLIDO")
    return 0
    
if __name__ == "__main__":
    main()
