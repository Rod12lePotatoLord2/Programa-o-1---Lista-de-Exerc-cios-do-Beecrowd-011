# Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

# Entrada
# O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

# Saída
# Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade. Assim como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

NotaA = float(input()) # Variável flutuante da primeira nota do aluno
NotaB = float(input()) # Variável flutuante da segunda nota do aluno
NotaC = float(input()) # Variável flutuante da terceira nota do aluno

MEDIA = ((NotaA * 2) + (NotaB * 3) + (NotaC * 5)) / 10 # Faz a soma ponderada das 3 notas do aluno e divide por 10 para calcular a média do aluno

print(f"MEDIA = {MEDIA:.1f}") #Imprime a média com apenas uma casa decimal após a vírgula.