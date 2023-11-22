'''Faça um programa que leia um ano e informe se ele é bissexto ou não.
Regras para o ano BISSEXTO
- Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
- Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
- Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.'''

def f_bissexto():
    #declaração de variáveis
    ano = int(0)
    #entrada de dados
    ano = int(input())
    #processamento
    if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        resultado = "É BISSEXTO"
    else:
        resultado = "NÃO É BISSEXTO"
    return resultado

def main():
    #saída de dados
    print(f'{f_bissexto()}')
    return 0

if __name__ == "__main__":
    main()