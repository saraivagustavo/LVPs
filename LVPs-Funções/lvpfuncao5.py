'''Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721. Usar, exclusivamente, DIV e MOD.'''

def f_tamanho(x):
    tamanho = 0 #inicialização da variável acumuladora
    #processamento
    while(x > 0):
        x = x // 10
        tamanho += 1
    return tamanho

def f_inverter(y):
    n_invertido = 0
    potencia = f_tamanho(y) - 1
    while(y > 0):
        resto = y % 10
        n_invertido += resto * 10 ** potencia
        y = y // 10
        potencia -= 1
    return n_invertido

def main():
    #entrada de dados
    numero = int(input("Digite um número: "))
    #saída de dados e invocação da função
    print(f'Número invertido: {f_inverter(numero)}')
    return 0
    
if __name__ == "__main__":
    main()