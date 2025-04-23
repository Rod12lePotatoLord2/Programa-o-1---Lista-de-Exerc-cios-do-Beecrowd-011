# Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

# Entrada
# A entrada contém 20 valores inteiros, positivos ou negativos.

# Saída
# Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.

N = [int(input()) for _ in range(20)]
for i in range(10):
    N[i], N[19 - i] = N[19 - i], N[i]
for i, valor in enumerate(N):
    print(f'N[{i}] = {valor}')

# A lista N é preenchida com 20 números inteiros digitados pelo usuário.
# A estrutura de compreensão de listas [int(input()) for _ in range(20)] faz o seguinte:
# for _ in range(20): repete 20 vezes.
# int(input()): em cada repetição, lê uma entrada do usuário (input()), converte para inteiro e adiciona na lista.
# Aqui acontece a inversão dos elementos da lista, do tipo "espelho":
# O loop vai de i = 0 até i = 9 (primeira metade da lista).
# N[i] representa os primeiros elementos.
# N[19 - i] representa os últimos elementos.
# A linha N[i], N[19 - i] = N[19 - i], N[i] faz a troca dos elementos simétricos: o primeiro com o último, o segundo com o penúltimo, e assim por diante.
# Depois disso, a lista N estará invertida
# No for i, valor in enumerate a lista N (agora invertida) é exibida no formato N[0] = ..., N[1] = ... N[19] = ...
# O enumerate(N) retorna o índice i e o valor valor ao mesmo tempo.
# Em resumo:
# O código Lê 20 números inteiros. Inverte a ordem dos elementos da lista. E imprime cada elemento com seu índice.