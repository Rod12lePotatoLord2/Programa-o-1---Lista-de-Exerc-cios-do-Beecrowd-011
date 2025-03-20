# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

# Fórmula: MaiorAB = (a + b + abs(a - b)) / 2

# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

maior1 = (a+b+abs(a-b))/2
maior2 = (maior1+c+abs(maior1-c))/2

print('{} eh o maior'.format(int(maior2)))

# O .split() divide a string em 3 partes, separando por espaços. O resultado é uma lista de três elementos, que são atribuídos às variáveis a, b e c.
# a, b e c são variáveis convertidas de strings em valores inteiros
# maior1 irá calcular a e b usando a formula e então irá armazenar o maior número entre eles
# maior2 irá calcular o maior 1 e c usando a fórmula e então irá armazenar o maior valor entre os três números fornecidos
# O maior valor, armazenado em maior2, é convertido para inteiro e impresso na tela.
# A função format() é usada para inserir esse valor na string '{} eh o maior'. [Forma antga de f']