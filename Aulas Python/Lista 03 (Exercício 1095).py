# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo
# I=1 J=60
# I=4 J=55
# I=7 J=50
# ...
# I=? J=0

I, J = 1, 60
while J >= 0:
    print(f'I={I} J={J}')
    I += 3
    J -= 5

# As variáveis I e J são iniciadas com os valores 1 e 60.
# A condição do laço while fará com que ele continue enquanto o valor de J for maior ou igual a zero.
# Quando J for menor que zero, o laço irá parar.
# A cada iteração do laço, o código irá imprimir os valores atualizados de I e J com a função print
# A cada iteração o valor de I recebe um incremento de 3
# A cada iteração o valor de J recebe um decrécimo de 5