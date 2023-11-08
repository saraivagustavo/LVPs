'''O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.'''

def main():
    #declaração de variáveis
    fabrica = float(0.0)
    distribuidor = float(0.0)
    impostos = float(0.0)

    #entrada de dados
    fabrica = float(input("Preço de fábrica: "))
    
    #processamento
    distribuidor = fabrica * (28 / 100)
    impostos = fabrica * (45 / 100)
    total = fabrica + distribuidor + impostos
    
    #saída de dados
    print(f'Preço final: {total}')
    return 0
    
if __name__ == "__main__":
    main()