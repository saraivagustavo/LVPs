'''Faça um programa que verifique os números de 1 a 5000 (ambos incluídos), identificando os que são quadrados perfeitos e capicuas (capicuas é aquilo que lido de trás para frente é a mesma coisa: 121, 1001, 4334, etc.)'''

def f_tamanho(x):
    #declaração de variáveis
    tamanho = int(0)
    tamanho = 0 #inicialização da variável acumuladora
    #processamento
    while(x > 0):
        x = x // 10
        tamanho += 1
    return tamanho
    
def f_inverter(y):
    #declaração de variáveis
    n_invertido = int(0)
    potencia = int(0)
    resto = int(0)
    
    n_invertido = 0 #inicialização da variável acumuladora
    
    #descobrir o tamanho do número (processamento)
    potencia = f_tamanho(y) - 1
    while(y > 0):
        resto = y % 10
        n_invertido += resto * 10 ** potencia
        y = y // 10
        potencia -= 1
    return n_invertido
    
def f_capicua(x):
    if(x == f_inverter(x) and x >= 10):
        return True
    return False
    
def f_qperfeito(x):
    #declaração de variáveis
    y = int(0)
    
    y = 1 #inicialização da variável acumuladora
    
    #processamento
    while(y ** 2 <= x):
        if(y ** 2 == x):
            return True
        y += 1
    return False
    
def main():
    #declaração de variáveis
    numero = int(0)
    
    #entrada de dados
    for numero in range(1,5001):
        if(f_capicua(numero) and f_qperfeito(numero)):
            print(f'{numero} É CAPICUA E QUADRADO PERFEITO')
        elif(f_capicua(numero)):
            print(f'{numero} É CAPICUA')
        elif(f_qperfeito(numero)):
            print(f'{numero} É QUADRADO PERFEITO')
    return 0
    
if __name__ == "__main__":
    main()