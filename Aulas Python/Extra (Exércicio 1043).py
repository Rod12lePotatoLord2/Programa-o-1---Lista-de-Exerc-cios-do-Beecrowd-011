# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
#
# Perimetro = XX.X
#
# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
#
# Area = XX.X
#
# Entrada
# A entrada contém três valores reais.
#
# Saída
# O resultado deve ser apresentado com uma casa decimal.

A, B, C = map(float, input().split())

if A + B > C and A + C > B and B + C > A:
    perimetro = A + B + C
    print(f'Perimetro = {perimetro:.1f}')
else:
    area = ((A + B) * C) / 2
    print(f'Area = {area:.1f}')

# A primeira linha digitada pelo usuário terá valores númericos que serão lidos e então divididos por espaço.
# Cada valor inserido será convertido em float (número decimal) e armazenado nas variáveis A, B e C.
# O Bloco if verifica se os três valores formam um triângulo válido, usando a desigualdade triangular: A soma de dois lados tem que ser maior que o terceiro, para todos os lados.
# Se isso for verdadeiro: O perímetro do triângulo será calculado. Em seguida ele é impresso com uma casa decimal
# Caso contrário: A área do triângulo será calculada. Em seguida ela é impressa com uma casa decimal