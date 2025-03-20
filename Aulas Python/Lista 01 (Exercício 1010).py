# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

# Entrada
# O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

# Saída
# A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

codigo1, numero1, valor1 = input().split()
codigo2, numero2, valor2 = input().split()

codigo1 = int(codigo1)
numero1 = int(numero1)
valor1 = float(valor1)

codigo2 = int(codigo2)
numero2 = int(numero2)
valor2 = float(valor2)

valor_total = (numero1 * valor1) + (numero2 * valor2)

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')

# O .split irá separar o código, o número e o valor
# O código e o número das peças são valores inteiros
# O valor das peças é um valor flutuante que será impresso com 2 casas após a vírgula
# O valor total é a soma entre os produtos dos números e valores das peças