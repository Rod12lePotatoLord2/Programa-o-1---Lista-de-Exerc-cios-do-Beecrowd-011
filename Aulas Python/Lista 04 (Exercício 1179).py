# Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.
#
# Entrada
# A entrada contém 15 números inteiros.
#
# Saída
# Imprima a saída conforme o exemplo abaixo.
#
# Exemplo de Entrada	Exemplo de Saída
# 1                     par[0] = 4
# 3                     par[1] = -4
# 4                     par[2] = 2
# -4                    par[3] = 8
# 2                     par[4] = 2
# 3                   impar[0] = 1
# 8                   impar[1] = 3
# 2                   impar[2] = 3
# 5                   impar[3] = 5
# -7                  impar[4] = -7
# 54                  impar[0] = 789
# 76                  impar[1] = 23
# 789                   par[0] = 54
# 23                    par[1] = 76
# 98                    par[2] = 98

# Inicializa duas listas vazias: uma para números ímpares e outra para pares.
impar = []
par = []

# Lê 15 números inteiros usando input() e converte para inteiro.
for _ in range(15): # Números pares vão para par, ímpares para impar. Quando a lista atinge 5 elementos, imprime os elementos no formato par[i] = x ou impar[i] = x e a lista é esvaziada.
    numero = int(input())
    if numero % 2 == 0:
        par.append(numero)
        if len(par) == 5:  # Imprime a lista de pares e esvazia
            for i, num in enumerate(par):
                print(f'par[{i}] = {num}')
            par = []
    else:
        impar.append(numero)
        if len(impar) == 5: # Imprime a lista de ímpares e esvazia
            for i, num in enumerate(impar):
                print(f'impar[{i}] = {num}')
            impar = []

for i, num in enumerate(impar):  # Imprime os números ímpares restantes
    print(f'impar[{i}] = {num}')
for i, num in enumerate(par):  # A mesma coisa só que com os pares
    print(f'par[{i}] = {num}')