'''Faça um programa, em Python 3.x, que receba uma letra minúscula. Para esse programa, crie uma função, baseado na Tabela ASCII, converta letras minúsculas em maiúsculas (NÃO É PERMITIDO O USO DO MÉTODO .upper())
Dica: pesquisem sobre as funções ord() e chr()'''

def f_maiusculo_wagner(t): #em vez de pegar uma letra só, pega cada letra de uma palavra e transforma em maiusculo
    nova = ""
    for i in range(len(t)):
        if(ord(t[i]) > 96):
            letra = chr(ord(t[i]) - 32)
            nova += letra
        else:
            nova += t[i]
    return nova

def f_converter_maiuscula(letra):
    codigo_ascii = ord(letra) #pega o código da letra minúscula na tabela ascii
    codigo_maiuscula = codigo_ascii - 32 #pega o código da mesma letra na tabela ascii só que em maiúsculo
    letra_maiuscula = chr(codigo_maiuscula) #pega a letra da tabela ascii pelo código da letra maiúscula
    return letra_maiuscula

def main():
    #declaração de variáveis
    letra = str("")
    maiuscula = str("")
    
    #entrada de dados
    letra = input()
    
    #invocação da função
    maiuscula = f_maiusculo_wagner(letra)
    
    #saída de dados
    print(f"{maiuscula}")
    return 0
    
if __name__ == "__main__":
    main()