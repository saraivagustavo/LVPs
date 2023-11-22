'''Utilizando strings e reconstrução de strings, elabore um programa em python que simule um jogo de forca. O programa deve solicitar uma palavra ao usuário desafiante (pesquise uma forma de apagar a "tela" console logo após a palavra chave ser infomada). O usuário desafiado tem 6 chances de erro para tentar acertar a palavra. Apenas os erros serão contabilizados.
 - Detalhes do jogo:
 O jogo termina quando o usuário usar as seis chances de erro ou quando ganhar o jogo.
Caso o usuário vença, deve ser informado o número de jogadas que ele tentou (inclusive os erros)
Apresente o sublinhado de tamanho da palavra procurada, use espaços em branco entre os sublinhados, pra facilitar a visualização
A cada jogada certa a letra correta deve aparecer na posição do sublinhado, onde ela está na palavra chave.
A cada jogada errada, as letras incorretas devem ser apresentadas abaixo dos sublinhados.'''

def f_criaForca(segredo):
    n = ""
    for i in range(len(segredo)):
        n += "_"
    return n

#----------

def f_testaLetra(forca,segredo,letra):
    n = ""
    for i in range(len(segredo)):
        if(letra == segredo[i]):
            n += letra
        else:
            n += forca[i]
    return n

#----------

def f_print(f):
    for i in range(len(f)):
        print(f[i],end=" ")
    print()
    
#----------

def f_vitoria(segredo,forca):
    if(segredo == forca):
        return True
    else:
        return False
        
#----------        

def f_verifica(letra,segredo):
    for i in range(len(segredo)):
        if(letra == segredo[i]):
            return True
    return False

#----------

def main():
    #declaração de variáveis
    erros = int(0)
    segredo = str("")
    letra = str("")
    forca = str("")
    letras_erradas = str("")
    #entrada de dados e processamento
    erros = 0
    segredo = input().upper()   
    forca = f_criaForca(segredo)
    cont = 0
    while(erros < 6 and f_vitoria(segredo,forca) == False):
        f_print(forca)
        print(letras_erradas)
        letra = input().upper()
        forca = f_testaLetra(forca,segredo,letra)
        if(f_verifica(letra,segredo) == False):
            letras_erradas += letra
            erros += 1
        cont += 1
    #saída de dados
    if(f_vitoria(segredo,forca)):
        for i in range(len(segredo)):
            print(segredo[i],end=" ")
        print(f'Parabéns, você ganhou com {cont} jogadas')
    else:
        f_print(forca)
        print(letras_erradas)
        print(f'Que pena, você não acertou a palavra {segredo}')
    return 0
    
if __name__ == "__main__":
    main()