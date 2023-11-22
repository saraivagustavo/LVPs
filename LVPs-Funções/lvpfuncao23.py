'''Faça um programa, em Python 3.x, que receba strings e, a partir de uma função, escreva uma nova STRING com as vogais (de forma não repetida) antes das consoantes  A condição de parada é quando for informada uma string vazia (""). Exemplo: input= PARALELEPIPEDO | output= AEIOPRLLPPD'''

def f_naoExiste(letra,vogal):
    for i in range(len(vogal)):
        if(letra == vogal[i]):
            return False
    return True

#----

def f_vogais(texto):
    #declaração de variáveis
    vogal = str("")
    vogais = str("")
    #inicialização da vaiável
    vogal = 'AEIOU'
    vogais = ''
    for i in range (len(texto)):
        for j in range(len(vogal)):
            if(texto[i] == vogal[j]):
                if(f_naoExiste(texto[i],vogais) == True):
                    vogais += texto[i]
    return vogais

#----

def f_naoVogal(letra,v):
    for i in range(len(v)):
        if(letra == v[i]):
            return False
    return True

#----

def f_removeVogais(vogal,texto):
    #declaração de variáveis
    consoantes = str("")
    #inicialização da variável
    consoantes = ''
    for i in range(len(texto)):
        if(f_naoVogal(texto[i],vogal)):
            consoantes += texto[i]
    return consoantes

#----

def f_alteraTexto(texto):
    #declaração de variáveis
    novo = str("")
    vogais = str("")
    consoantes = str("")
    
    vogais = f_vogais(texto)
    consoantes = f_removeVogais(vogais,texto)
    return vogais+consoantes
    
#----    
    
def main():
    #declaração de variáveis
    texto = str("")
    #entrada de dados
    texto = input().upper()
    while(texto != ''):
        print(f_alteraTexto(texto))
        texto = input().upper()
    return 0
    
if __name__ == "__main__":
    main()