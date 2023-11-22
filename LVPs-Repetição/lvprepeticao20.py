'''Deseja-se fazer um levantamento a respeito da ausência de alunos à primeira prova de Programação de Computadores para as N turmas de existentes no Ifes.
O valor de N é fornecido pelo usuário. O valor de N (quantidade de turmas) é o primeiro dado fornecido ao usuário.
Para cada uma das N turmas existentes é fornecido um conjunto de valores nesta ordem:
 - a identificação da turma - tipo (string);
 - a quantidade de alunos matriculados - tipo (int);
Os demais dados desta turma são:
 - a matrícula de um aluno - tipo (string)
 - a frequência do aluno - a letra A (ausente) ou a letra P (presente) - tipo (string)
Fazer um programa que:
 - Para cada uma das N turmas (N diversas turmas), calcule a porcentagem de ausência dos alunos. Imprima a identificação da turma e a porcentagem, calculada, de ausência de alunos com duas casas decimais.
 - Determine e imprima qual turma teve a (primeira) maior porcentagem de ausência. Imprima a turma e sua respectiva porcentagem com duas casas decimais.
 - Determine e imprima qual turma teve a (primeira) menor porcentagem de ausência. Imprima a turma e sua respectiva porcentagem com duas casas decimais.
 - Determine e imprima quantas turmas tiveram porcentagem de ausência superior a 20%.'''

def main():
    #declaração de variáveis
    n = int(0)
    turmas = int(0)
    turma = str("")
    qntd = int(0)
    alunos = int(0)
    matricula = str("")
    frequencia = str("")
    conta_ausencia = int(0)
    perc_ausencia = float(0.0)
    maior_20 = int(0)
    turma_maior = str("")
    turma_menor = str("")
    
    #entrada de dados e processamento
    n = int(input("Quantidade de turmas: "))
    for turmas in range(0,n,1):
        #obtendo nome da turma e quantidade de alunos da turma
        turma = input("Identificação da turma: ")
        qntd = int(input("Quantidade de alunos da turma: "))
        conta_ausencia = 0
        #obtendo dados de ausência e presença dos alunos da turma
        for alunos in range(0,qntd,1):
            matricula = input("Matrícula do aluno: ")
            frequencia = input("Frequência do aluno <A/P>: ")
            #contando a quantidade de ausentes da turma
            if(frequencia.upper() == "A"):
                conta_ausencia += 1
        #cálculo do percentual da ausência da turma
        perc_ausencia = conta_ausencia * 100 / qntd
        #nome da turma e o percentual de ausência dela
        print(f'TURMA={turma} AUSENCIA=  {perc_ausencia:.2f} %')
        #verificando qual turma tem maior e menor percentual de ausência
        if(turmas == 0): #a primeira turma é a maior e menor ao mesmo tempo
            maior_perc = perc_ausencia
            menor_perc = perc_ausencia
        elif(perc_ausencia > maior_perc):
            maior_perc = perc_ausencia
            turma_maior = turma
        elif(perc_ausencia < menor_perc):
            menor_perc = perc_ausencia
            turma_menor = turma        
        #verificando quantas turmas tiveram percentual maior que 20%
        if(perc_ausencia > 20):
            maior_20 += 1
            
    #saída de dados    
    print(f'TURMA COM MAIOR % DE AUSENCIA= {turma_maior} AUSENCIA= {maior_perc:.2f} %')
    print(f'TURMA COM MENOR % DE AUSENCIA= {turma_menor} AUSENCIA= {menor_perc:.2f} %')
    print(f'{maior_20} TURMAS COM % DE AUSENCIA SUPERIOR A 20%')
    return 0

if __name__ == "__main__":
    main()