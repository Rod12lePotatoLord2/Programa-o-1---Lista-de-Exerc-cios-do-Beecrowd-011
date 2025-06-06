# eia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
# se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
# se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
# se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

# Entrada
# A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

# Saída
# Imprima todas as classificações do triângulo especificado na entrada.

# Lê 3 valores númericos float
A, B, C = map(float, input().split())

# Organiza os lados em ordem decrescente
lados = sorted([A, B, C], reverse=True)
A, B, C = lados[0], lados[1], lados[2]

# Verifica se um triângulo pode ser formado
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Verifica o tipo do triângulo com base em seus ângulos
    if A ** 2 == B ** 2 + C ** 2:
        print("TRIANGULO RETANGULO")
    if A ** 2 > B ** 2 + C ** 2:
        print("TRIANGULO OBTUSANGULO")
    if A ** 2 < B ** 2 + C ** 2:
        print("TRIANGULO ACUTANGULO")

    # Busca tipos específicos de triângulos com base na largura de suas laterais
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")