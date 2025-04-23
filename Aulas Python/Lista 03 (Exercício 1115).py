# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

# Entrada
# A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

# Saída
# Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.
# Entrada              Saída
# 2 2                 primeiro
# 3 -2                 quarto
# -8 -1               terceiro
# -7 1                segundo
# 0 2

while True:
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        break
    elif x > 0 and y > 0:
        print('primeiro')
    elif x < 0 and y > 0:
        print('segundo')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x > 0 and y < 0:
        print('quarto')

# O laço while True cria um loop infinito que só será interrompido quando uma condição break for atingida. Dentro do loop, o programa vai ler os valores de x e y repetidamente.
# O comando x, y vai ler uma linha de entrada onde dois valores são fornecidos separados por espaço, usando a função split() para dividir a entrada e a função map(int, ...) para converter essas strings em números inteiros e armazenando os valores em x e y.
# Caso algum dos valores de x ou y seja igual a 0, o programa interrompe a execução do loop usando o comando break.
# Essa condição if é usada para parar o programa quando uma entrada que envolva a origem do plano cartesiano (onde x ou y são zero) for fornecida.
# Se nenhum dos valores for zero, o programa entra em uma série de condições elif para determinar em qual quadrante o ponto (x, y) se encontra:
# Se tanto x quanto y forem positivos, o programa imprime "primeiro".
# Se x for negativo e y for positivo, o programa imprime "segundo".
# Se tanto x quanto y forem negativos, o programa imprime "terceiro".
# Se x for positivo e y for negativo, o programa imprime "quarto".