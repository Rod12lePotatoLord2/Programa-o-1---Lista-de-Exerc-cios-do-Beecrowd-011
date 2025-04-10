# Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las. O processo é muito simples. São feitas três passadas em todo o texto.

# Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

# Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”. O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

# Entrada
# A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de linhas que o problema deve tratar. As N linhas contém cada uma delas M (1 ≤ M ≤ 1*103) caracteres.

# Saída
# Para cada entrada, deve-se apresentar a mensagem criptografada.

N = int(input())

for _ in range(N):
    P = input()

    novoP = ""
    for letra in P:
        novoP += chr(ord(letra) + 3) if letra.isalpha() else letra
    P = novoP[::-1]
    P = P[:len(P)//2] + ''.join([chr(ord(letra) - 1) for letra in P[len(P)//2:]])

    print(P)

# A variável N indica um valor inteiro deve ser inserido pelo usuário
# for _ in range(): é um loop que se repetirá N vezes (Uma vez para cada palavra)
# Dentro do loop a variável P irá armazenar a string que será transformada
# novoP = "" vai aplicar uma transofrmação para cada caractere na string P
# letra.isalpha() vai verificar se o caractere é uma letra (de A a Z ou de a a z).
# Se a letra for uma letra do alfabeto, o código aplica a transformação chr(ord(letra) + 3), movendo a letra 3 posições à frente na tabela
# Caso a letra não seja uma letra, ela não se altera.
# Após esse loop, a string novoP contém a versão transformada de P, onde todas as letras foram deslocadas por 3 posições à frente.
# P = novoP[::-1] irá criar uma cópia invertida da string P
# P[:len(P)//2] pega a primeira metade da string invertida, sem alterações.
# Já a segunda metade, passará por outra transformação. Para cada letra dessa segunda metade, o código aplica chr(ord(letra) - 1), deslocando a letra uma posição para trás na tabela.