# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

# Entrada
# O arquivo de entrada contém dois valores inteiros.

# Saída
# O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

X = int(input().strip())
Y = int(input().strip())

soma = 0
if X > Y:
    for i in range (X -1, Y, -1):
        if i % 2 != 0:
            soma += i
else:
    for i in range (X+1, Y):
        if i % 2 != 0:
            soma += i

print(soma)

# X e Y são valores inteiros inseridos pelo usuário
# .strip() é uma função que remove qualquer espaço extra que venha antes ou após o número digitado
# Variável soma tem valor inicial 0
# A condicional if irá verificar se X é maior que Y
# Caso sim, um loop será executado percorrendo todos os valores númericos entre X-1 e Y (Não incluso) em ordem decrescente graças ao -1 no range
# Condicional if i % 2 != 0 verifica se o número é ímpar (Resto da divisão é diferente de 0)
# Caso sim, ele será somado à variável soma
# Caso X seja menor do que Y, o else irá executar um loop percorrendo todos os valores númericos entre X+1 e Y (Não incluso) em ordem crescente
# Condicional if i %2 != 0 fará a mesma coisa que no outro loop
# Se o número for ímpar, ele será somado à variàvel soma
# print fará a impressão da mensagem na tela