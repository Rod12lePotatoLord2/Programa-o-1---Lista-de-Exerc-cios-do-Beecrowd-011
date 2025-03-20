# Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

# Entrada
# O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem (em horas) e o segundo é a velocidade média durante a mesma (em km/h).

# Saída
# Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

x = int(input()) # Tempo gasto na viagem em horas
y = float(input()) # Velocidade média na viagem em km/h

litros =  (x * y) / 12 # multiplica o tempo gasto pela velocidade média para calcular a distância percorrida. Em seguida, a distância é dividida por 12, que é o número de quilômetros que o veículo percorre por litro de combustível, para determinar quantos litros de combustível serão necessários

print(f'{litros:.3f}')
