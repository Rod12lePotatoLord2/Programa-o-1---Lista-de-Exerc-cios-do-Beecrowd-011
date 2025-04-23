# Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

# Saída
# Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.

def is_prime(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input())
for _ in range(n):
    x = int(input())
    if is_prime(x):
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')

# A função definida vai verificar se um número é primo:
# Números menores que 2 (como 0 e 1) não são primos.
# Para os demais, a função testa divisores de 2 até a raiz quadrada de numero, pois não é necessário verificar além disso para determinar a primalidade.
# Se encontrar algum número que divida numero sem resto, ele não é primo.
# Se nenhum divisor for encontrado, então é primo.
# O programa lê N, a quantidade de números inseridos pelo usuário que serão testados.
# Para cada número x, ele chama a função is_prime(x).
# Baseado no retorno, imprime se x "eh primo" ou "nao eh primo"