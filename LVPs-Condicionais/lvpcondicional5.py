'''Ler quatro valores referentes a quatro notas escolares (0 a 100) de um aluno e escrever uma mensagem dizendo que o aluno foi APROVADO se o valor da média escolar for maior ou igual a 60, Se o aluno teve média inferior a 60, informar que ele está reprovado.'''

def main():
    #declaração de variáveis
    nota1 = float(0.0)
    nota2 = float(0.0)
    nota3 = float(0.0)
    nota4 = float(0.0)
    media = float(0.0)
    
    #entrada de dados
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    nota4 = float(input())
    
    #processamento de dados
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    #saída de dados
    if (media > 60):
        print('APROVADO')
    else:
        print('REPROVADO')
    return 0

if __name__ == "__main__":
    main()