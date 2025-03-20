# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

# Obs: Utilize ponto (.) para separar a parte decimal.

N = float(input()) # Valor decimal (float) como entrada, que representa o valor total que será separado em em notas e moedas. O valor pode incluir centavos.

# Notas

notas_de_100 = N//100  # Mesma lógica do Exercício 1018
N = N%100

notas_de_50 = N//50
N = N%50

notas_de_20 = N//20
N = N%20

notas_de_10 = N//10
N = N%10

notas_de_5 = N//5
N = N%5

notas_de_2 = N//2
N = N%2

# Moedas

moedas_de_1_centavo = N//1  # Mesma lógica das notas, porém com valores decimais (Centavos)
N = N%1

moedas_de_50_centavos = N//0.50
N = N%0.50

moedas_de_25_centavos = N//0.25
N = N%0.25

moedas_de_10_centavos = N//0.1
N = N%0.1

moedas_de_5_centavos = N//0.05
N = N%0.05

moedas_de_01_centavos = N/0.01

print('NOTAS:')
print(f'{int(notas_de_100)} nota(s) de R$ 100.00')
print(f'{int(notas_de_50)} nota(s) de R$ 50.00')
print(f'{int(notas_de_20)} nota(s) de R$ 20.00')
print(f'{int(notas_de_10)} nota(s) de R$ 10.00')
print(f'{int(notas_de_5)} nota(s) de R$ 5.00')
print(f'{int(notas_de_2)} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{int(moedas_de_1_centavo)} moeda(s) de R$ 1.00')
print(f'{int(moedas_de_50_centavos)} moeda(s) de R$ 0.50')
print(f'{int(moedas_de_25_centavos)} moeda(s) de R$ 0.25')
print(f'{int(moedas_de_10_centavos)} moeda(s) de R$ 0.10')
print(f'{int(moedas_de_5_centavos)} moeda(s) de R$ 0.05')
print(f'{moedas_de_01_centavos:.0f} moeda(s) de R$ 0.01')

# O comando print(f'{int(notas_de_100)} nota(s) de R$ 100.00') vai imprimir a quantidade de cédulas de R$ 100.00, por exemplo.
# O número de cédulas e moedas é convertido para inteiro usando int() para que o valor não seja exibido com casas decimais.
# A formatação para moedas de 1 centavo é diferente:
# O valor é arredondado para zero casas decimais usando a formatação .0f, garantindo que o número de moedas de 1 centavo seja exibido corretamente.
# O código utiliza divisão inteira (//) para calcular as cédulas e módulo (%) para obter o restante de cada valor. O mesmo conceito é aplicado a moedas.