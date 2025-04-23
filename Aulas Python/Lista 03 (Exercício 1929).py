# Ana e suas amigas estão fazendo um trabalho de geometria para o colégio, em que precisam formar vários triângulos, numa cartolina, com algumas varetas de comprimentos diferentes. Logo elas perceberam que não dá para formar triângulos com três varetas de comprimentos quaisquer: se uma das varetas for muito grande em relação às outras duas, não dá para formar o triângulo.

# Neste problema, você precisa ajudar Ana e suas amigas a determinar se, dados os comprimentos de quatro varetas, é ou não é possível selecionar três varetas, dentre as quatro, e formar um triângulo.

# Entrada
# A entrada é composta por apenas uma linha contendo quatro números inteiros A, B, C e D (1 ≤ A, B, C, D ≤ 100).

# Saída
# Seu programa deve produzir apenas uma linha contendo apenas um caractere, que deve ser ‘S’ caso seja possível formar o triângulo, ou ‘N’ caso não seja possível formar o triângulo.

A, B, C, D = map(int, input().split())

def forma_triangulo(x, y, z):
    return x + y > z and x + z > y and y + z > x

if (forma_triangulo(A, B, C) or
        forma_triangulo(A, B, D) or
        forma_triangulo(A, C, D) or
        forma_triangulo(B, C, D)):
    print('S')
else:
    print('N')

# A entrada lê quatro números inteiros em uma única linha, separados por espaço, e os atribui às variáveis A, B, C e D. Eles representam os comprimentos de quatro segmentos de reta.
# A função def forma_triangulo verifica se três segmentos com comprimentos x, y e z podem formar um triângulo.
# Ela usa a condição da desigualdade triangular, que diz que: A soma de dois lados de um triângulo deve ser maior que o terceiro lado.
# Se as três condições forem verdadeiras, a função retorna True, ou seja, os três segmentos formam um triângulo válido.
# A condicional if vai testar todas as combinações possíveis de 3 lados escolhidos entre os 4 disponíveis (A, B, C, D)
# Se qualquer uma delas retornar True, a mensagem 'S' será impressa, caso contrário a mensagem 'N' será impressa em seu lugar