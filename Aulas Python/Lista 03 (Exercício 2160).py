# Preencher formulários é uma tarefa simples. Mas é preciso conferir se o espaço reservado para os dados é suficiente.

# Sua tarefa é, dada uma linha de texto, indicar se ele cabe ou não cabe em um formulário com 80 caracteres.

# Entrada
# A entrada é uma linha de texto L (1 ≤ |L| ≤ 500).

# Saída
# A saída é dada em uma única linha. Ela deve ser "YES" (sem as aspas) se a linha de texto L tem até 80 caracteres. Se L tem mais de 80 caracteres, a saída deve ser "NO".

L = input()
if len(L) <= 80:
    print('YES')
else:
    print('NO')

# A variável L será uma linha de texto inserida pelo usuário
# A função len() é usada na condicional if para contar quantos caracteres há em L.
# Se o comprimento for menor ou igual a 80, a mensagem 'YES' será impressa na tela.
# Se o comprimento for igual a 80, a mensagem 'YES' será impressa na tela.
# Caso contrário, a mensagem 'NO' será impressa na tela.