# Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
# S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# A saída contém um valor correspondente ao valor de S.
# O valor deve ser impresso com dois dígitos após o ponto decimal.

S = 0
numerador = 1
denominador = 1

for _ in range(20):
    S += numerador / denominador
    numerador += 2
    denominador *= 2

print(f'{S:.2f}')

# O valor inicial da variável S é 0
# Os valores iniciais das variáveis numerador e denominador serão respectivamente 1 e a cada iteração serão atualizados (numerador recebrá um acrescimo de 2, já o denominador será multiplicado por 2)
# O laço for irá iterar 20 vezes, representando o cálculo de 20 termos da sequência.
# A cada iteração, o valor de numerador / denominador é somado à variável S
# Os valores de ambos serão atualizados com as iterações (numerador recebendo uma adição de 2 e o denominador dobrando)
# O print irá imprimir o valor de S após as 20 iterações, formatado para 2 casas decimais