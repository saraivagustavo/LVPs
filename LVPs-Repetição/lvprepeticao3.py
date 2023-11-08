'''Faça um Programa que leia números até que o usuário não queira mais digitar os números. No final escrever a soma dos valores lidos. (o usuário digitará a letra s para continuar informando dados e n quando quiser parar)'''

def main():
    #declaração de variáveis
    flag = str('')
    numero = int(0)
    soma = int(0)
    
    soma = 0 #incialização da variável controladra
    flag = input("Deseja informar um número (s/n): ") #inicialização da variável de controle
    while(flag == 's'): #condição de parada
        #entrada de dados
        numero = int(input("Digite o número: "))
        #processamento
        soma = soma + numero
        flag = input("Deseja informa outro número (s/n): ") #atualização da variável de controle
    print(f'{soma}')
    return 0
    
if __name__ == "__main__":
    main()