'''Faça um programa que receba 4 (quatro) notas de um aluno (0 a 100) e apresente a sua média aritmética final.'''

def main():
    #declaração de variáveis
    nota1 = float(0.0)
    nota2 = float(0.0)
    nota3 = float(0.0)
    nota4 = float(0.0)
    media = float(0.0)
    
    #entrada de dados
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))
    
    #processamento
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    #saída de dados
    print(f'Média = {media}')
    return 0
    
if __name__ == "__main__":
    main()