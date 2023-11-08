'''Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo e qual tipo de triângulo é. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.'''

def main():
    #declaração de variáveis
    ladoa = int(0)
    ladob = int(0)
    ladoc = int(0)
    somaab = int(0)
    somaac = int(0)
    somabc = int(0)

    #entrada de dados
    ladoa = int(input())
    ladob = int(input())
    ladoc = int(input())

    #processamento
    somaab = ladoa + ladob
    somaac = ladoa + ladoc
    somabc = ladob + ladoc

    #saída de dados
    if(ladoa > somabc or ladob > somaac or ladoc > somaab):
         print('NÃO É TRIÂNGULO')
    else:
         if((ladoa == ladob and ladob != ladoc) or (ladoa == ladoc and ladoc != ladob) or (ladob == ladoc and ladoc != ladoa)):
              print('ISÓSCELES')
         else:
              if(ladoa == ladob and ladob == ladoc):
                   print('EQUILÁTERO')
              else:
                   print('ESCALENO')
    return 0

if __name__ == "__main__":
     main()  