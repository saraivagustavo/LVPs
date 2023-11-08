'''Considere um programa que solicite uma STRING e, em seguida, solicita uma letra ao usuário (converta para maiúsculo na entrada), para inclusão em uma string por exemplo, porém, essa letra só será adicionada a string, caso ela não exista na referida cadeia de caracteres. O programa deve ser elaborado para funcionar com qualquer string pré existente. Faça uma validação de entrada, em Python 3.x, que valide o input do usuário da seguinte forma: caso o usuário digite uma letra que já existe na string, exiba a mensagem "LETRA EXISTENTE, DIGITE OUTRA", e caso ele informe uma letra que ainda não se encontra na cadeia de caracteres, apresenta  a mensagem "LETRA INEXISTENTE". Ao final, exibir a string modificada.'''

from verificacao import f_verificaLetra

def main():
    #declaração de variáveis
    texto = str("")
    letra = str("")
    
    #entrada de dados
    texto = input().upper()
    letra = input().upper()
    
    #processamento e saída de dados
    while(f_verificaLetra(letra,texto) == True):
        print("LETRA EXISTENTE, DIGITE OUTRA")
        letra = input().upper()
    print("LETRA INEXISTENTE")
    texto = texto + letra
    print(f'{texto}')
    return 0

if __name__ == "__main__":
    main()