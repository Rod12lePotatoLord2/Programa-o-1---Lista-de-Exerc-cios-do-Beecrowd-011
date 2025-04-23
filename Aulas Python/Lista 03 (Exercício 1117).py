# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

# Entrada
# A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.

# Saída
# Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
# Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.

notas_validas = []
while len(notas_validas) < 2:
    nota = float(input())
    if 0 <= nota <= 10:
        notas_validas.append(nota)
    else:
        print('nota invalida')

media = sum(notas_validas) / 2
print(f'media = {media:.2f}')

# A variável notas_validas é uma lista vazia. Ela vai armazenar as duas notas válidas que o usuário digitar
# O programa entra em um laço while que só será interrompido quando o número de notas válidas na lista for igual a 2.
# Ou seja, o laço vai se repetir até que duas notas válidas sejam recebidas.
# A função input() na variável nota lê a entrada do usuário como uma string e, em seguida, a função float() converte essa string em um número de ponto flutuante (decimal)
# A condicional if verifica se a nota inserida está dentro do intervalo de 0 a 10 (inclusive).
# Se a nota for válida, ela é adicionada à lista notas_validas com o comando append().
# Caso contrário, o programa imprime a mensagem 'nota invalida' e solicita que o usuário insira uma nova nota.
# O comando .append é utilizado para adicionar um único elemento ao final de uma lista
# Após o laço ser interrompido (ou seja, quando duas notas válidas forem fornecidas), a média das duas notas é calculada.
# A função sum(notas_validas) soma os valores das duas notas, e depois o resultado é dividido por 2 para calcular a média.
# Por fim, o print irá imprimir o resultado da média calculada em 2 casas decimais