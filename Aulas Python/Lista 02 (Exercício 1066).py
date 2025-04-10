# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

par = 0
impar = 0
positivo = 0
negativo = 0

for _ in range(5):
    valor = int(input())

    if valor % 2 == 0:
        par += 1
    else:
        impar += 1

    if valor > 0:
        positivo += 1
    elif valor < 0:
        negativo += 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')

# par, impar, positivo e negativo são variáveis com valor 0. Serão usadas para contar quantos números
# for é um laço que irá iterar 5 vezes. A cada iteração o usuário vai inserir um número inteiro. Ele será guardado na variável valor.
# if irá conferir se o valor será par, caso não seja, o else determinará que ele é ímpar
# if irá conferir se o valor será positivo, caso não seja, o else if verá se ele é negativo
# print vai imprimir os resultados na tela