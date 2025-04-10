# Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

# Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda.

# Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

# Saída
# Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".

imposto = float(input())

if 0 <= imposto <= 2000:
    print('Isento')

elif 2000 < imposto <= 3000:
    valor_excedente_1 = imposto - 2000
    valor1 = valor_excedente_1 * 0.08
    print(f'R$ {valor1:.2f}')

elif 3000 < imposto <= 4500:
    valor_excedente_1 = 3000 - 2000
    valor_excedente_2 = imposto - 3000
    valor1 = valor_excedente_1 * 0.08
    valor2 = valor_excedente_2 * 0.18
    valor_final = valor1 + valor2
    print(f'R$ {valor_final:.2f}')

else:
    valor_excedente_1 = 3000 - 2000
    valor_excedente_2 = 4500 - 3000
    valor_excedente_3 = imposto - 4500
    valor1 = valor_excedente_1 * 0.08
    valor2 = valor_excedente_2 * 0.18
    valor3 = valor_excedente_3 * 0.28
    valor_total_final = valor1 + valor2 + valor3
    print(f'R$ {valor_total_final:.2f}')

# O input solicita que o usuário insira um valor referente ao rendimento ou valor base sobre o qual o imposto será calculado.
# O float vai converter o valor inserido pelo usuário para um número de ponto flutuante (caso o usuário digite um número com casas decimais).
# Se o valor do imposto estiver entre 0 e 2000, o contribuinte é isento de pagar qualquer imposto. O código irá imprimir a mensagem 'Isento'.
# Se o valor do imposto estiver entre 2000 e 3000, o cálculo do imposto é feito sobre o valor excedente de 2000. Ou seja, o valor acima de 2000 será tributado a 8%.
# O valor_excedente_1 = imposto - 2000 irá calcular o valor excedente a 2000.
# O valor1 = valor_excedente_1 * 0.08 vai aplicar uma alíquota (percentual) de 8% sobre o valor excedente.
# O código então imprime o imposto devido, formatado com duas casas decimais
# Se o valor do imposto estiver entre 3000 e 4500, o código calculará o imposto em duas etapas:
# O valor excedente a 2000 até 3000 será tributado a 8%.
# O valor excedente a 3000 até 4500 será tributado a 18%.
# O valor_excedente_1 = 3000 - 2000: Valor que será tributado a 8% (de 2000 a 3000).
# O valor_excedente_2 = imposto - 3000: Valor que será tributado a 18% (de 3000 a 4500).
# O valor1 = valor_excedente_1 * 0.08: Calcula o imposto sobre o valor de 2000 a 3000 (8%).
# O valor2 = valor_excedente_2 * 0.18: Calcula o imposto sobre o valor de 3000 a 4500 (18%).
# O valor_final = valor1 + valor2: Soma os dois valores de imposto e exibe o resultado formatado com duas casas decimais.
# Caso o valor do imposto esteja acima de 4500, o cálculo do imposto será feito em três etapas:
# Os mesmos cálculos do anterior com uma adição:
# O valor acima de 4500 será tributado a 28%.
# O valor_excedente_3 = imposto - 4500: Calcula o valor que será tributado a 28%.
# Mesma coisa para calcular o percentual dos dois primeiros valores
# O valor3 = valor_excedente_3 * 0.28: Aplica a alíquota (percentual) de 28% sobre o valor acima de 4500.
# O valor_total_final soma os três valores de imposto e exibe o total a ser pago, formatado com duas casas decimais.