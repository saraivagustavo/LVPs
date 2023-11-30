'''Faça um programa, em Python 3.x, que leia um valor inteiro entre 1000 (MIL) e 9999 (NOVE MIL NOVECENTOS E NOVENTA E NOVE) (inclusive os dois valores)  e, utilizando apensa recursos  matemáticos (DIV:  % e MOD: //) que já aprendemos em sala de aula, inverta esse número, entregando um valor inteiro como resposta (NÃO É PERMITIDO UTILIZAR QUALQUER RECURSO DE STRING OU MÉTODO/FUNÇÃO NÃO APRENDIDOS E USADOS NA DISCIPLINA, EM CASO DE USO, A QUESTÃO TERÁ NOTA ZERO). Ao final, o programa deverá verificar se o valor digitado é uma CAPICUA, imprimindo a informação conforme os casos de teste.
CAPICUA: sequência de algarismos que permanece a mesma se lida na ordem direta ou inversa (p.ex., 13231).'''

def main():
    #declaração de variáveis
    numero = int(0)
    unidade = int(0)
    dezena = int(0)
    centena = int(0)
    milhar = int(0)
    parte = int(0)
    inversao = int(0)

    #entrada de dados
    numero = int(input())

    #processamento
    unidade = numero % 10
    print(f'unidade: {unidade}')
    parte = numero // 100
    print(f'parte: {parte}')
    dezena = parte % 10
    print(f'dezena: {dezena}')
    milhar = numero // 1000
    print(f'milhar: {milhar}')
    centena = parte % 10
    print(f'centena: {centena}')
    inversao = unidade * 1000 + dezena * 100 + centena * 10 + milhar
    
    #saída de dados
    if(inversao == numero):
        print(f'{numero} É UMA CAPICUA')
    else:
        print(f'{numero} NÃO É UMA CAPICUA')
    return 0

if __name__ == "__main__":
    main()