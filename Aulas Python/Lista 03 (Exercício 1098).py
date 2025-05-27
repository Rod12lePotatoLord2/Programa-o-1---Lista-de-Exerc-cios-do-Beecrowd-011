# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo.
# I=0 J=1
# I=0 J=2
# I=0 J=3
# I=0.2 J=1.2
# I=0.2 J=2.2
# I=0.2 J=3.2
# .....
# I=2 J=?
# I=2 J=?
# I=2 J=?

for beecrowd in range(11):
    i = beecrowd * 0.2
    for j in range(1, 4):
        x = i + j
        if i == int(i):
            print(f'I={int(i)} J={int(x)}')
        else:
            print(f'I={i:.1f} J={x:.1f}')

# O for beecrowd é um laço externo vai de 0 a 10 (inclusive), ou seja, 11 iterações. Em cada iteração, ele gera o valor de i multiplicando o índice por 0.2
# O for j é um laço  interno que vai de 1 a 3. Para cada valor de i, ele calcula x = i + j.
# A condicional if verifica se i é um número inteiro (por exemplo, 1.0 == 1) Para formatar corretamente a saída:
# Se i for um inteiro, imprime sem casas decimais.
# Caso contrário, imprime com uma casa decimal (.1f).