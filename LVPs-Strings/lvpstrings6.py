'''Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.'''

def main():
    #declaração de variáveis
    data = str("")
    dia = int(0)
    mes = int(0)
    ano = int(0)
    
    #entrada de dados
    data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:])
    if(mes == 1):
        print(f'{dia} de janeiro de {ano}')
    elif(mes == 2):
        print(f'{dia} de fevereiro de {ano}')
    elif(mes == 3):
        print(f'{dia} de março de {ano}')
    elif(mes == 4):
        print(f'{dia} de abril de {ano}')
    elif(mes == 5):
        print(f'{dia} de maio de {ano}')
    elif(mes == 6):
        print(f'{dia} de junho de {ano}')
    elif(mes == 7):
        print(f'{dia} de julho de {ano}')
    elif(mes == 8):
        print(f'{dia} de agosto de {ano}')
    elif(mes == 9):
        print(f'{dia} de setembro de {ano}')
    elif(mes == 10):
        print(f'{dia} de outubro de {ano}')
    elif(mes == 11):
        print(f'{dia} de novembro de {ano}')
    elif(mes == 12):
        print(f'{dia} de dezembro de {ano}')
    return 0
    
if __name__ == "__main__":
    main()
    