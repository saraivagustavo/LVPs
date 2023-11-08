'''Faça um programa, em Python 3.x, que leia a massa (Kg) e a força (em Newtons), submetidas sobre um corpo.  e informe qual é a aceleração que ele adquire;'''

def main():
    #declaração de variáveis
    massa = float(0.0)
    forca = float(0.0)
    aceleracao = float(0.0)
    
    #entrada de dados
    massa = float(input("Digite a massa: "))
    forca = float(input("Digite a força: "))
    
    #processamento
    aceleracao = forca / massa
    
    #saída de dados 
    print(f'Aceleração = {aceleracao} m/s²')
    return 0
    
if __name__ == "__main__":
    main()