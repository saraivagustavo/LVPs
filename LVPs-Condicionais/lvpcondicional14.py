def main():
    #declaração de variáveis
    litros = float(0.0)
    tipo = str
    precoa = float(0.0)
    precog = float(0.0)

    #entrada de dados
    litros = float(input())
    tipo = input()
    
    #processamento de dados
    precoa = litros * 2.9
    precog = litros * 3.3
    
    #saída de dados
    if((litros <= 20) and (tipo == 'A')):
        print(precoa * 0.97)
    else:
        if((litros > 20) and (tipo == 'A')):
            print(precoa * 0.95)
    
    if((litros <= 20) and (tipo == 'G')):
        print(precog * 0.96)
    else:
        if((litros > 20) and (tipo == 'G')):
            print(precog * 0.94)
                
    return 0
    
if __name__ == "__main__":
    main()