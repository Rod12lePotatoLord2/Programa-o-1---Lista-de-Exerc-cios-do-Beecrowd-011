# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

# Entrada
# O arquivo de entrada contém um valor inteiro N.

# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

N = int(input()) # Tempo total em segundos
horas = N // 3600 # Divide o total pela quantidade de segundos em uma hora (ou seja 3600)
minutos = (N % 3600) // 60 # O % vai calcular o resto da divisão de N por 3600. Esse valor representa os segundos restantes após subtrair as horas completas. Depois, dividimos esse valor por 60 (o número de segundos em um minuto) usando a divisão inteira //, para calcular quantos minutos completos existem nos segundos restantes.
segundos = N % 60 # Calcula o resto da divisão anterior, revelando os segundos restantes (Descartando horas e minutos completos)

print(f'{horas}:{minutos}:{segundos}')


# // Símbolo da divisão inteira