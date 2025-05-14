# Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.
#
# Entrada
# A entrada será um valor inteiro positivo.
#
# Saída
# A saída será uma sequência de seis números ímpares.
#
# Exemplo de Entrada	Exemplo de Saída
# 8                             9
#                               11
#                               13
#                               15
#                               17
#                               19

X = int(input())

if X % 2 == 0:  # Se X for par, adicione 1 para torná-lo ímpar
    X += 1

for i in range(6):
    print(X)
    X += 2  # Incrementa para o próximo número ímpar