'''Faça um programa que solicite que o usuário digite a resposta para uma pergunta (S ou N). Na entrada altere esse valor para maiúsculo. Faça uma validação de entrada, em Python 3.x, que valide o input do usuário da seguinte forma: caso o usuário digite uma alternativa inválida, exiba as mensagens conforme os casos de teste, abaixo'''

def main():
    #declaração de variáveis
    resposta = str("")
    
    #entrada de dados
    resposta = input().upper()
    
    #processamento e saída de dados
    while(resposta != "S" and resposta != "N"):
        print(f"RESPOSTA INCORRETA, DIGITE S OU N")
        resposta = input().upper()
    if(resposta == "S" or resposta == "N"):
        print(f"RESPOSTA CORRETA")
    return 0
    
if __name__ == "__main__":
    main()