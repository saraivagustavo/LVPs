'''Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado, UTILIZANDO DIV E MOD. SEM USAR RECURSO DE STRING'''

def f_tamanho(x):
    #declaração de variáveis
    tamanho = int(0)
    tamanho = 0 #inicialização da variável acumuladora
    #processamento
    while(x > 0):
        x = x // 10
        tamanho += 1
    return tamanho

def main():
    #declaração de variáveis
    numero = int(0)
    #entrada de dados
    numero = int(input("Digite um número: "))
    #saída de dados e invocação da função
    print(f'N° de algarismos: {f_tamanho(numero)}')
    return 0
    
if __name__ == "__main__":
    main()