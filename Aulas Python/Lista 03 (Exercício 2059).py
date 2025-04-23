# Um novo jogo chamado Ímpar, Par ou Roubo (IPR) está se tornando muito popular. Esse jogo surgiu quando alguns amigos estavam sem conexão com a internet, sem celular, sem computador e bastante desocupados. O jogo está tão popular que irá acontecer um campeonato mundial de IPR e cada país do mundo irá escolher um representante para competir.

# O jogo funciona da seguinte forma: dois jogadores participam, o jogador 1 escolhe entre par ou ímpar, então cada jogador escolhe um inteiro positivo, se a soma desses números for par e o jogador 1 tiver escolhido par então o jogador 1 ganha, se a soma for ímpar o jogador 2 ganha. Caso o jogador 1 tivesse escolhido ímpar ele ganharia se a soma fosse ímpar, caso a soma fosse par o jogador 2 ganharia. Nada de diferente de um jogo de par ou ímpar convencional, correto?

# A diferença do jogo é que o jogador 1 pode roubar e assim assegurar sua vitória independentemente do resultado do jogo de ímpar ou par convencional, já o jogador 2 pode ou não acusar o jogador 1 de roubo. Com essas adições no jogo se o jogador 1 roubar e o jogador 2 acusar o roubo então o jogador 2 ganha, caso o jogador 2 não acuse o roubo e o jogador 1 roubar então o jogador 1 ganha, caso o jogador 2 acuse o roubo, mas o jogador 1 não tiver roubado então o jogador 1 ganha, se o jogador 1 não roubar e o jogador 2 não acusar o roubo o jogo segue como descrito anteriormente.

# Você foi contratado pela OIIPR (Organização Internacional de Ímpar, Par ou Roubo) para desenvolver um programa que dada a escolha do jogador 1 entre par ou ímpar, os números escolhidos como jogada e as ações dos jogadores (roubo/acusação) mostre quem foi o vencedor.

# Entrada
# A entrada consite de uma única linha contendo 5 inteiros: p, j1, j2, r, a. ( 0 ≤ p, r, a ≤ 1 e 1 ≤ j1, j2 ≤ 100).

# p representa a escolha do jogador 1 (se p = 1 então o jogador 1 escolheu par, se p = 0 então o jogador 1 escolheu ímpar). Os valores j1, j2, representam respectivamente o número escolhido pelo jogador 1 e pelo jogador 2. r representa se o jogador 1 roubou (se r = 1 então o jogador 1 roubou, se r = 0 então o jogador 1 não roubou), a representa se o jogador 2 acusou o roubo (se a = 1 então o jogador 2 acusou o jogador 1 de roubo, se a = 0 então ele não acusou o jogador 1 de roubo).

# Saída
# Imprima "Jogador 1 ganha!" se o jogador 1 ganhou ou "Jogador 2 ganha!" se o jogador 2 ganhou (sem as aspas).

p, j1, j2, r, a = map(int, input().split())

if r == 1 and a == 1:
    print('Jogador 2 ganha!')
elif r == 1 and a == 0:
    print('Jogador 1 ganha!')
elif r == 0 and a == 1:
    print('Jogador 1 ganha!')
else:
    soma = j1 + j2
    if (soma % 2 == 0 and p == 1) or (soma % 2 != 0 and p == 0):
        print('Jogador 1 ganha!')
    else:
        print('Jogador 2 ganha!')

# O programa lê cinco valores inteiros: p, j1, j2, r e a
# p: 1 se o Jogador 1 escolheu "par", 0 se escolheu "ímpar".
# j1: número escolhido pelo Jogador 1.
# j2: número escolhido pelo Jogador 2.
# r: 1 se o Jogador 1 tentou roubar, 0 caso contrário.
# a: 1 se o Jogador 2 acusou o roubo, 0 caso contrário.
# Regras do Jogo:
# Se o Jogador 1 tentou roubar (r == 1) e o Jogador 2 acusou (a == 1):  O Jogador 2 ganha.
# Se o Jogador 1 tentou roubar (r == 1) mas o Jogador 2 não acusou (a == 0): O Jogador 1 ganha (roubo bem-sucedido 😅).
# Se o Jogador 1 não tentou roubar (r == 0) mas foi acusado (a == 1): O Jogador 1 ganha (acusação falsa).
# Se ninguém roubou e ninguém acusou: A soma dos números de j1 + j2 define o resultado com base em par ou ímpar:
# Se a soma for par (soma % 2 == 0) e p == 1, o Jogador 1 ganha.
# Se a soma for ímpar (soma % 2 != 0) e p == 0, o Jogador 1 ganha.
# Caso contrário, o Jogador 2 ganha