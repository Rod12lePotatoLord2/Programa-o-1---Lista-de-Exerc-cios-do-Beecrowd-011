# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo
# I=1 J=7
# I=1 J=6
# I=1 J=5
# I=3 J=7
# I=3 J=6
# I=3 J=5
# ...
# I=9 J=7
# I=9 J=6
# I=9 J=5

for i in range(1, 10, 2):
    for j in range(7, 4, -1):
        print(f'I={i} J={j}')

# Esse código tem 2 laços for que criarão sequências de números
# O for i in range irá criar uma sequência de 1 a 9, contando de 2 em 2. Seus valores são 1,3,5,7,9
# O for j in range irá criar uma sequência de 7 a 5 (4 não incluso), subtraindo 1 a cada passo. Seus valores são 7,6,5
# Por fim, o print irá imprimir os valores atuais formatados de i e j na string