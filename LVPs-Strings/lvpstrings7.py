'''Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
    A)quantos espaços em branco existem na frase.
    B)quantas vezes aparecem as vogais a, e, i, o, u.'''

def main():
    #declaração de variáveis
    frase = str("")
    cont_espaco = int(0)
    cont_a = int(0)
    cont_e = int(0)
    cont_i = int(0)
    cont_o = int(0)
    cont_u = int(0)

    #inicialização das variáveis acumuladoras
    cont_espaco = 0
    cont_a = 0
    cont_e = 0
    cont_i = 0
    cont_o = 0
    cont_u = 0

    #entrada de dados e processamento
    frase = input().upper()
    for i in range(len(frase)):
        if(frase[i] == " "):
            cont_espaco += 1
        elif(frase[i].upper() == "A"):
            cont_a += 1
        elif(frase[i].upper() == "E"):
            cont_e += 1
        elif(frase[i].upper() == "I"):
            cont_i += 1
        elif(frase[i].upper() == "O"):
            cont_o += 1
        elif(frase[i].upper() == "U"):
            cont_u += 1  
    print(f'ESPAÇOS EM BRANCO = {cont_espaco}')   
    print(f'A = {cont_a}')   
    print(f'E = {cont_e}')   
    print(f'I = {cont_i}')   
    print(f'O = {cont_o}')  
    print(f'U = {cont_u}')  
    return 0

if __name__ == "__main__":
    main()
    
