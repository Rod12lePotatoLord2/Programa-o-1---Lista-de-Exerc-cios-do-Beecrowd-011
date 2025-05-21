# Um grupo de cientistas está fazendo novas experiências para criar uma nave que possibilite a viagem muito mais rápida até Marte do que é possível atualmente. Esta nave utilizará dois foguetes e um novo combustível recém criado, muito mais eficiente que os utilizados até hoje. Só que a velocidade que os novos foguetes podem proporcionar à nave está relacionada diretamente com o peso do combustível armazenado nestes foguetes (em kg) e, por incrível que pareça, uma relação deste peso com números primos. Por exemplo, se o peso total do combustível dos foguetes for 1010 kg, a velocidade atingida (em km/h) é a soma dos 10 números primos à partir de 1010 (incluindo ele se for primo): 1013 -> 1019 -> 1021 -> 1031 -> 1033 -> 1039 -> 1049 -> 1051 -> 1061 -> 1063, ou seja, 10380 km/h.
#
# Os cientistas estão muito intrigados com esta relação matemática existente e querem que você construa um programa que calcule quanto tempo aproximado (em horas e em dias) uma nave levaria para ir da terra até marte com este novo combustível, dado um determinado peso de foguetes (claro, eles estão tentando criar os maiores foguetes possíveis) assumindo que a distância da terra até marte no dia do lançamento, será 60 milhões de kms.
#
# Entrada
# A entrada contém um único valor inteiro Peso (1000 < Peso ≤ 60000) indicando o peso máximo de combustível (em kg) que os foguetes podem armazenar.
#
# Saída
# A saída esperada consiste em duas linhas. A primeira linha contém a velocidade que pode ser atingida pela nave, seguida pelo texto "km/h". A segunda linha contém o tempo estimado de viagem até Marte em horas e em dias (truncados), com mensagem de texto correspondente, conforme o exemplo abaixo.
# Exemplos de Entrada	Exemplos de Saída
# 1010                     10380 km/h
#                         5780 h / 240 d
# 60000                    600578 km/h
#                           99 h / 4 d

def eh_primo(n): # Essa função verifica se um número é primo usando a verificação por tentativa de divisão até a raiz quadrada do número.
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def soma_dos_10_primos_a_partir_de(peso): # Essa função começa a partir do número peso e vai somando os primos que encontrar (pulando os que não são primos). Para quando tiver somado os 10 primeiros primos a partir dali.
    primos = []
    atual = peso
    while len(primos) < 10:
        if eh_primo(atual):
            primos.append(atual)
        atual += 1
    return sum(primos)

def calcular_tempo(velocidade): # velocidade é a soma dos 10 primos.
    distancia = 60000000  # 60 milhões de km
    tempo_horas = distancia // velocidade # Tempo (em horas) = 60 milhões dividido pela velocidade
    tempo_dias = tempo_horas // 24 # Converte para dias inteiros, divide por 24 e descarta os decimais
    return tempo_horas, tempo_dias

peso = int(input())

velocidade = soma_dos_10_primos_a_partir_de(peso)
horas, dias = calcular_tempo(velocidade)

print(f'{velocidade} km/h')
print(f'{horas} h / {dias} d')
