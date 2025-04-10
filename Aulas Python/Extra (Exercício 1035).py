# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

# Entrada
# Quatro números inteiros A, B, C e D.

# Saída
# Mostre a respectiva mensagem após a validação dos valores.

A, B, C, D = map(int, input().split())

if B > C and D > A and (C + D > A + B) and C > 0 and D > 0 and A % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

# map(int, input().split()) será usado para ler os valores inteiros inseridos de A, B, C, D
# Condição if irá verificar se:
# B é maior que C
# D é maior que A
# Soma de C e D é maior que a soma de A + B
# C é positivo (Maior que 0)
# D é positivo (Maior que 0)
# A é par
# Se todas as condições forem verdadeiras, a mensagem 'Valores aceitos' será impressa
# Caso alguma das condições seja falsa, a mensagem 'Valores nao aceitos' será impressa