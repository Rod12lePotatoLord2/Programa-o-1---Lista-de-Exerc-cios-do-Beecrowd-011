# Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

# O símbolo ( representa "maior que". Por exemplo:
# [0,25]  indica valores entre 0 e 25.0000, inclusive eles.
# (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

# Entrada

# O arquivo de entrada contém um número com ponto flutuante qualquer.

# Saída

# A saída deve ser uma mensagem

N = float(input())

if 0<= N <= 25:
    print(f'Intervalo [0,25]')

elif 25 < N <= 50:
    print(f'Intervalo (25,50]')

elif 50 < N <= 75:
    print(f'Intervalo (50,75]')

elif 75 < N <= 100:
    print(f'Intervalo (75,100]')

else:
    print(f'Fora de intervalo')

# A variável N é um string que será inserido pelo usuário, então será convertido para um ponto flutuante (Número Decimal)
# if 0<= N <= 25 é uma condicional que irá verificar se N está no intervalo entre 0 e 25, ou seja se ele é maior/igual a 0 e menor/igual a 25
# Se essa condição se provar verdadeira, a mensagem 'Intervalo [0,25]' será impressa, provando que N está nesse intervalo
# O mesmo vale para os outros elif
# Caso N não satisfaça nenhuma das condições anteriores, a mensagem 'Fora de intervalo' será impressa