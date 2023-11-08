'''Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.'''

def main():
    #declaração de variáveis
    total = int(0)
    brancos = int(0)
    nulos = int(0)
    validos = int(0)
    brancospct = float(0.0)
    nulospct = float(0.0)
    validospct = float(0.0)
    
    #entrada de dados
    total = int(input("Digite o total de votos: "))
    brancos = int(input("Digite o total de votos brancos: "))
    nulos = int(input("Digite o total de votos nulos: "))
    validos = int(input("Digite o total de votos válidos: "))
    
    #processamento
    brancospct = brancos / total
    nulospct = nulos / total
    validospct = validos / total
    
    #saída de dados
    print(f'BRANCOS = {brancospct * 100} %')
    print(f'NULOS = {nulospct * 100} %')
    print(f'VALIDOS = {validospct * 100} %')
    return 0
    
if __name__ == "__main__":
    main()