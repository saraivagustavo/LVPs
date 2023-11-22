'''Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo. A última linha que não entrará nos cálculos, contém o valor da idade igual a zero. Calcule e escreva a idade média deste grupo de indivíduos.'''

def main():
    #declaração de variáveis
    idade = int(0)
    soma = int(0)
    media = float(0.0)
    
    #inicialização de variáveis
    soma = 0 #variável acumuladora
    i = 0 #variável de controle
    idade = 1
    
    #entrada de dados
    while(idade != 0): #condição de parada
        idade = int(input("Digite a idade (ou 0 para sair): "))
        if(idade != 0):
            soma += idade #atualização da variável acumuladora
            i += 1 #atualização da variável de controle

    if(i != 0):   
        media = soma / i
    
    print(f'A média das idades é: {media:.1f}')
    return 0
    
if __name__ == "__main__":
    main()
