'''A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas, totalizando o esperado de 160h/mês).'''

def main():
    #declaração de variáveis
    horas_trabalhadas = int(0)
    salario_hora = float(0.0)
    
    #entrada de dados
    horas_trabalhadas = int(input())
    salario_hora = float(input())
 
    #saída de dados
    if(horas_trabalhadas <= 160):
        print(horas_trabalhadas * salario_hora)
    else:
        print((horas_trabalhadas * salario_hora) + ((horas_trabalhadas - 160) * (salario_hora * 0.5)))
        
    return 0

if __name__ == "__main__":
    main()
    