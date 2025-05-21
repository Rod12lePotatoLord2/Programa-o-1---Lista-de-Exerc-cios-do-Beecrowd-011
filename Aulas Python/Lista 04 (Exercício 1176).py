# Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.
#
# Entrada
# A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste. Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60), correspondente ao N-esimo termo da série de Fibonacci.
#
# Saída
# Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o N-ésimo termo da série de Fibonacci.
#
# Exemplo de Entrada	Exemplo de Saída
# 3                      Fib(0) = 0
# 0                      Fib(4) = 3
# 4                      Fib(2) = 1
# 2

fib = [0,1] # Inicia a lista com os dois primeiros números da sequência: Zero e Um
penultimo = 0 # Penúltimo número (Fib(n-2))
ultimo = 1    # Último número (Fib(n-1))
for i in range(60): # Calcula mais 60 números (já temos 2, então no total: 62). Após isso, a lista fib terá os valores de Fib(0) até Fib(61).
    novo = ultimo + penultimo
    fib.append(novo)
    penultimo = ultimo
    ultimo = novo
num_de_casos_teste = int(input()) # O usuário digita quantos números de Fibonacci ele quer consultar.

for i in range(num_de_casos_teste): # Para cada caso de teste, lê um índice e imprime o Fibonacci correspondente.
    enesimo_fib = int(input())
    print(f'Fib({enesimo_fib}) = {fib[enesimo_fib]}')