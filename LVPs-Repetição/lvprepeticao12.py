'''Faça um Programa que leia números até que o usuário não queira mais digitar os números. No final escrever a soma dos valores positivos e a média dos valores negativos.  (o usuário digitará a letra s para continuar informando dados e n quando quiser parar)'''

def main():
    # Declaração de variáveis
    soma_positivos = int(0) 
    soma_negativos = int(0) 
    media_negativos = float(0.0)
    cont_negativos = int(0)
    numero = int(0)
    flag = str("") #variável de controle
    
    #inicialização das variáveis deacumuladoras
    cont_negativos = 0 #inicialização da variável de controle dos NÚMEROS NEGATIVOS
    soma_positivos = 0 
    soma_negativos = 0 

    # Entrada de dados
    flag = input("Deseja informar um número? (s/n): ") #inicialização da variável de controle
    while(flag.upper() == "S"): #condição de parada
        numero = int(input("Digite um número: "))
        if(numero >= 0): #considerando zero como positivo
            soma_positivos += numero
        else:
            soma_negativos += numero
            cont_negativos += 1 #atualização da variável de controle dos números NEGATIVOS
        flag = input("Deseja informar outro número? (s/n): ") #atualização da variável de controle

    if(cont_negativos > 0):
        media_negativos = soma_negativos / cont_negativos  
    else:
        media_negativos = 0
    print(f'Soma dos positivos: {soma_positivos}')
    print(f'Média dos negativos: {media_negativos}')
    #print(f'{soma_positivos} {media_negativos}')

if __name__ == "__main__":
    main()
