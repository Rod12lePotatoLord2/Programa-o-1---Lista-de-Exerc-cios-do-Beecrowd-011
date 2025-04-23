# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo.
# I=1 J=7
# I=1 J=6
# I=1 J=5
# I=3 J=9
# I=3 J=8
# I=3 J=7
# ...
# I=9 J=15
# I=9 J=14
# I=9 J=13

for i in range(1, 10, 2):
    for j in range(i + 6, i + 3, -1):
        print(f'I={i} J={j}')

# Esse código possui 2 laços que criarão sequências de números
# O for i in range irá criar uma sequência de 1 a 9, contando de 2 em 2. Seus valores são 1,3,5,7,9
# O for j in range cria uma sequência que começa em i + 6, vai até i + 3 (não incluindo), com um passo de -1.
# Ou seja, para cada valor de i, o laço interno percorre de i + 6 até i + 4, decrementando em 1
# Dentro do segundo laço, o comando print imprime os valores atuais de i e j, formatados na string