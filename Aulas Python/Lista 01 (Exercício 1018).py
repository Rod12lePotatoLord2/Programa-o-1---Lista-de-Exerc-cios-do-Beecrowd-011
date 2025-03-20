# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

N = int(input())  # N é um inteiro que representa o valor total que irá separar o valor em cédulas

print(f'{N}')  # imprime o valor que foi inserido pelo usuário, para confirmação

notas_de_100 = N // 100  # N é dividido por 100 usando divisão inteira (//), o que retorna o número de cédulas de R$ 100 necessárias.
N = N%100  # Em seguida, N é atualizado para o valor restante, após subtrair as cédulas de R$ 100, com a operação de módulo (%), que retorna o resto da divisão por 100

notas_de_50 = N // 50 # O mesmo ocorre para as demais notas. [A cada etapa, o valor de N é atualizado com o restante, após considerar as cédulas da denominação anterior]
N = N%50

notas_de_20 = N // 20
N = N%20

notas_de_10 = N // 10
N = N%10

notas_de_5 = N // 5
N = N%5

notas_de_2 = N // 2
N = N%2

print(f'{notas_de_100} nota(s) de R$ 100,00')
print(f'{notas_de_50} nota(s) de R$ 50,00')
print(f'{notas_de_20} nota(s) de R$ 20,00')
print(f'{notas_de_10} nota(s) de R$ 10,00')
print(f'{notas_de_5} nota(s) de R$ 5,00')
print(f'{notas_de_2} nota(s) de R$ 2,00')
print(f'{N} nota(s) de R$ 1,00')

# Finalmente, o código imprime o número de cédulas de cada valor (100, 50, 20, 10, 5, 2 e 1) necessárias para representar o valor original N