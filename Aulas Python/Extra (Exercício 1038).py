# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
# Código   Especificação    Preço
# 1        Cachorro Quente  R$ 4.00
# 2        X-Salada         R$ 4.50
# 3        X-Bacon          R$ 5.00
# 4        Torrada Simples  R$ 2.00
# 5        Refrigerante     R$ 1.50
# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

n1, n2 = map(int, input().split())

precos = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

total = n2 * precos[n1]

print(f'Total: R$ {total:.2f}')

# O input será um valor digitado pelo usuário
# O split vai dividir a linha em partes separadas por espaços
# O map(int) vai converter os valores digitados em números inteiros
# Os valores serão atribuidos as variáveis n1 e n2
# n1 será o código do produto
# n2 será a quantidade do produto desejado pelo usuário
# precos mostra os preços referentes a cada código da tabela
# precos[n1] acessará o valor do produto escolhido com o valor de n1
# o total irá multiplicar a quantidade pelo preço do produto e gerar o valor total a ser pago pelo usuário
# O print irá imprimir na tela o valor total calculado convertido para 2 casas decimais, garantindo que ele seja mostrado corretamente em forma de reais (R$)