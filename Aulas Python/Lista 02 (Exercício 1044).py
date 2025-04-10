# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

# Entrada
# A entrada contém valores inteiros.

# Saída
# A saída deve conter uma das mensagens conforme descrito acima.

A, B = map(int, input().split())

if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

# input lê a linha de entrada do usuário
# .split divide a linha em partes, separando por espaços
# map(int, converte essas strings em inteiros
# % calcula o resto da divisão
# A % B verifica se A é divisível por B, ou seja se o resto da divisão é zero
# B % A mesmo processo
# Condicional if vai verificar se essas informações são verdadeiras, se sim a primeira mensagem será impressa
# Caso contrário, a segunda mensagem será impressa