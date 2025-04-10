# Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

# Entrada
# A entrada contém um valor inteiro N (0 < N < 13).

# Saída
# A saída contém um valor inteiro, correspondente ao fatorial de N.

N = int(input())
fatorial = 1

for i in range(N, 0, -1):
    fatorial = fatorial * i

print(fatorial)

# A função input() irá ler a entrada do usuário
# A função int irá converter a entrada em um número inteiro (Nesse caso, o valor de N)
# A variável fatorial se inicia com o valor 1, o fatorial de um número é o produto de todos os inteiros de 1 até esse número, ele começará por 1, porque qualquer número multiplicado por 1 é ele mesmo.
# O for é um laço que vai iterar do valor N até 1, subtraindo de 1 em 1 a cada iteração.
# O comando range (N, 0, -1)  gera uma sequência de números começando de N até 1.
# Em cada iteração do laço, o valor de fatorial é multiplicado pelo valor atual de i. Acumulando o produto dos números de N até 1.
# print irá imprimir o valor na tela