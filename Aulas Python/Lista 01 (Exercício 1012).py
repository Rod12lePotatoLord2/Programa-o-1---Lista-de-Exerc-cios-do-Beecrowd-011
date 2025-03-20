# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

# Entrada
# O arquivo de entrada contém três valores com um dígito após o ponto decimal.

# Saída
# O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

area1, area2, area3 = input().split()
area1 = float(area1)
area2 = float(area2)
area3 = float(area3)

pi = 3.14159
TRIANGULO = (area1 * area3) / 2
CIRCULO = pi * (area3 ** 2)
TRAPEZIO = ((area1 + area2) * area3) / 2
QUADRADO = area2 ** 2
RETANGULO = area1 * area2

print(f'TRIANGULO: {TRIANGULO:.3f}')
print(f'CIRCULO: {CIRCULO:.3f}')
print(f'TRAPEZIO: {TRAPEZIO:.3f}')
print(f'QUADRADO: {QUADRADO:.3f}')
print(f'RETANGULO: {RETANGULO:.3f}')

# area1, area2, area3 divide a linha em 3 partes
# As variáveis area são convertidas em float ou seja permitindo que sejam calculadas
# area1 é a base e area3 é a altura, area2 é o lado
# Fórmula do Triângulo é calculada da seguinte forma: Base * Altura / 2
# Fórmula do Círculo é calculada da seguinte forma: pi * raio²
# Fórmula do Trapézio é calculada da seguinte forma: (base maior + base menor) * altura / 2
# Fórmula do Quadrado é calculada da seguinte forma: lado²
# Fórmula do Retângulo é calculada da seguinte forma: largura * altura (Nesse caso area1 é a largura e a area2 é a altura)