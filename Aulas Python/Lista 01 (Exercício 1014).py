# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

# Entrada
# O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

# Saída
# Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

X = int(input())
Y = float(input())

consumo = X / Y

print(f'{consumo:.3f} km/l')

# X será o valor referente a distância total percorrida em km
# Y será um valor flutuante referente ao combustível gasto no percurso
# A variável consumo representará o consumo médio do automóvel durante a viagem
# A mensagem impressa exibirá o valor do consumo médio, com 3 casa decimais representadas por :.3f
# {} é chamado de Máscara em Python