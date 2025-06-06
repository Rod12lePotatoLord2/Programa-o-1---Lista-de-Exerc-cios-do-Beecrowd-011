# Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.

# Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++), assumem que o resultado da divisão entre dois inteiros é outro inteiro.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante (dupla precisão), correspondente ao raio da esfera.

# Saída
# A saída deverá ser uma mensagem "VOLUME" conforme o exemplo fornecido abaixo, com um espaço antes e um espaço depois da igualdade. O valor deverá ser apresentado com 3 casas após o ponto.

raio_da_esfera = float(input())
pi = 3.14159
volume = (4/3) * pi * raio_da_esfera ** 3

print(f'VOLUME = {volume:.3f}')

# A fórmula para achar o volume é dada por: v = 4/3 * pi * raio³
# v é o volume
# raio_da_esfera é a variável flutuante que representa o raio
# pi é o número de pi