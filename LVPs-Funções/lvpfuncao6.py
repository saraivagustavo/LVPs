'''1) Faça um programa em Python3, DE FORMA MODULAR (DEFININDO E USANDO SUAS PRÓPRIAS FUNÇÕES), para resolver o seguinte problema:
a) Definir uma função em Python 3 que calcule o valor do fatorial de um número N inteiro maior ou igual a zero. Esta função recebe como parâmetro o valor de N. Esta função retorna o valor do fatorial de N calculado.
b) Faça um programa principal que leia diversos números inteiros maiores ou iguais a zero. Para cada número N lido imprima uma saída EXATAMENTE conforme o modelo apresentado nos casos de teste abaixo. A condição de parada da entrada de dados é ler um número N menor que zero.'''

def f_fatorial(n):  #esse "n" de dentro do parenteses, recebe a variável "numero" lá da função main e transforma ela na variável "n" da função f_fatorial
  #declaração de variável
  fatorial = int(0)
  #inicialização da variável acumuladora
  fatorial = 1
  #processamento
  while (n > 1):
    fatorial *= n
    n -= 1
  return fatorial

def main():
  #declaração de variáveis
  numero = int(0)
  resultado = int(0)

  #entrada de dados
  numero = int(input())
  resultado = f_fatorial(numero)  #esse "numero" de dentro do parenteses vai ser enviado para a função f_fatorial
  #saída de dados
  print(f'Fatorial({numero}) = {resultado}')
  return 0


if __name__ == "__main__":
  main()