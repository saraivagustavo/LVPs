'''Faça um programa que leia um valor inteiro de 100 a 999 (inclusive) e, utilizando recursos que já aprendemos em sala de aula, inverta esse número, entregando um valor inteiro de três casas decimais (PROIBIDO UTILIZAR QUALQUER RECURSO DE STRING). Ao final, o programa deverá verificar se o valor digitado é uma CAPICUA.'''

def main():
    #declaração de variáveis
    numero = int(0)
    centena = int(0)
    dezena = int(0)
    unidade = int(0)
    resto = int(0)
    inversao = int(0)
    
    #entrada de dados
    numero = int(input('digite um número: '))
    
    #processamento de dados
    centena = numero // 100
    print(f'{centena} = dígito da centena')#pegar o dígito da centena
    resto = numero // 10
    unidade = numero % 10
    print(f'{unidade} = dígito da unidade')#pegar o dígito da unidade
    print(f'{resto} = parte do número retirado para seleção do dígito da dezena')#pegar uma parte do número para retirar o dígito da dezena
    dezena = resto % 10
    print(f'{dezena} = dígito da dezena (com base no número todo digitado)')#pegar o dígito da dezena
    inversao = unidade * 100 + dezena * 10 + centena
    
    #saída de dados
    print(f'número invertido = {inversao}')
    if(inversao == numero):
        print(f'{numero} É UMA CAPICUA')
    else:
        print(f'{numero} NÃO É UMA CAPICUA')
        
    return 0

if __name__ == "__main__":
    main()
