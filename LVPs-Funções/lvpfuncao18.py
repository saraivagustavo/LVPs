'''Faça um programa que conte a incidência de um determinado número [0-9] dentro de um intervalo de valores, começando em 0 e o fim do intervalo determinado pelo usuário.'''

def f_incidencia(numero,inicio,fim):
    contador = 0
    numero_str = str(numero) #precisa transformar em string para pegar os números terminados ou que tenham no meio o digito desejado (ex: 19)
    for i in range(inicio, fim + 1):
        i_str = str(i) #precisa transformar em string também porque mudou o tipo da variável "numero"
        for digito in i_str:
            if digito == numero_str:
                contador += 1
    return contador

def main():
    #declaração de variáveis
    numero = int(0)
    inicio = int(0)
    fim = int(0)
    #entrada de dados
    numero = int(input())
    inicio = 0
    fim = int(input())
    #invocação da função
    quantidade = f_incidencia(numero, inicio, fim)
    #saída de dados
    print(f"{quantidade}")
    return 0
    
if __name__ == "__main__":
    main()