# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

# Distancia = raíz de (x2 - x1)² + (y2 - 1)² [Fórmula Euclidiana]

# Entrada
# O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

# Saída
# Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.

p1 = input().split()  # A função .split() divide a string em uma lista de substrings com base no espaço. [Ex: 1.0 , 2.0]
p2 = input().split()

x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

print(f'{distancia:.4f}')

# Cada coordenada (como strings) é convertida para um número de ponto flutuante usando a função float().
# Agora temos as variáveis x1, y1, x2, e y2 representando as coordenadas dos dois pontos no plano.
# Na fórmula euclidiana vai elevar ao quadrado a diferença entre as coordenadas.
# Esses quadrados são somados e, em seguida, a raiz quadrada do resultado é calculada com o operador (potência), que eleva o valor a 1/2 (equivalente à raiz quadrada)