# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
#
# Entrada
# A entrada contem três números inteiros.
#
# Saída
# Imprima a saída conforme foi especificado.
# Exemplo de Entrada	Exemplo de Saída
# 7 21 -14                  -14
#                             7
#                            21

numeros = list(map(int, input().split()))
ordenados = sorted(numeros)

print(f'{ordenados[0]}\n{ordenados[1]}\n{ordenados[2]}\n')
print(f'{numeros[0]}\n{numeros[1]}\n{numeros[2]}')

# O input() lê uma linha de entrada (Valores inseridos pelo usuário)
# O .split() divide a string com base nos espaços, resultando em uma lista de strings
# O map(int, ...) converte cada string em um número inteiro
# O list(...) transforma o resultado em uma lista
# Essa lista é armazenada na variável numeros.
# sorted(numeros) retorna uma nova lista com os números em ordem crescente.
# Essa nova lista é armazenada na variável ordenados.
# O print imprime os três números ordenados, um por linha.
# O \n no final da última linha adiciona uma linha em branco.