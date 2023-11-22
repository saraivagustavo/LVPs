'''Faça um Programa que leia números até que o usuário não queira mais digitar os números. No final escrever a soma dos valores positivos e a soma dos valores negativos.  (o usuário digitará a letra s para continuar informando dados e n quando quiser parar)'''

def main():
    #declaração de variáveis
    flag = str("")
    numero = int(0)
    soma_positivos = int(0)
    soma_negativos = int(0)
    
    #inicialização das variáveis
    soma_positivos = 0
    soma_negativos = 0
    
    #entrada de dados
    flag = input("Deseja informar um número? (s/n): ")
    while(flag.upper() == "S"):
        numero = int(input("Digite o número: "))
        if(numero > 0):
            soma_positivos += numero
        else:
            soma_negativos += numero
        flag = input("Deseja informar outro número? (s/n): ")
    
    #saída de dados
    print(f'{soma_positivos} {soma_negativos}')
    return 0

if __name__ == "__main__":
    main()