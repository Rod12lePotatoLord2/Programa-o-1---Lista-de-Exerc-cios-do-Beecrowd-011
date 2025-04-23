# Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação deve ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. A imagem abaixo ilustra o caso da entrada do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser considerados na operação.

# Entrada
# A primeira linha de entrada contem um número L (0 ≤ L ≤ 11) indicando a linha que será considerada para operação. A segunda linha de entrada contém um único caractere Maiúsculo T ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz, sendo que a mesma é preenchida linha por linha, da linha 0 até a linha 11, sempre da esquerda para a direita.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

linha = int(input())
operacao = input()

matriz = [[float(input()) for _ in range(12)] for _ in range(12)]

valores_da_linha = matriz[linha]
resultado = sum(valores_da_linha)

if operacao == 'M':
    resultado /= len(valores_da_linha)

print(f'{resultado:.1f}')

# A variável linha lê um número inteiro do usuário, que representa o índice da linha da matriz que será usada. Como é uma matriz 12x12, esse valor deve estar entre 0 e 11.
# A variável operação lê uma string do usuário, que indica a operação a ser feita com os valores da linha escolhida: 'S' para soma e 'M' para média
# A variável matriz é uma lista de listas que lê 144 valores (12 x 12) do usuário e os organiza numa matriz 12x12 de números float. (Cada lista interna representa uma linha da matriz)
# valores_de_linha vai pegar a linha específica (indicada pelo valor que o usuário digitou primeiro) da matriz.
# resultado vai somar todos os valores da linha escolhida
# Na condicional if: Se a operação for 'M', ele calcula a média dividindo a soma pela quantidade de elementos (nesse caso, 12).
# Por fim, o print irá imprimir o resultado formatado com uma casa decimal