# Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

# Entrada
# O arquivo de entrada contém 2 valores com uma casa decimal cada um.

# Saída
# Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

A = float(input()) #A função float converte o valor de A para um ponto flutuante, ou seja para um número com casas decimais.
B = float(input()) #A função float converte o valor de B para um número com casa decimais.

MEDIA = ((A * 3.5) + (B * 7.5)) / 11  # A variável MEDIA calcula a média entre os valores de A e B, com seus pesos específicos.

print(f"MEDIA = {MEDIA:.5f}")

# A * 3.5 é um cálculo que multiplica o valor de A pelo peso atribuido à ele (3.5)
# B * 7.5 é um cálculo que multiplica o valor de B pelo peso atribuido à ele (7.5)
# (A * 3.5) + (B * 7.5) soma os dois resultados dos cálculos anteriores. Dando uma soma ponderada de ambos
# /11 irá dividir por 11 a soma ponderada dos valores acima, normalizando o cálculo da média de forma correta.
# O f antes das aspas é uma f-string. Dentro delas podemos inserir expressões dentro das chaves {} e elas serão avaliadas e convertidas em uma string de forma automática.
# :.5f é um especificador de formato para controlar a maneira como o valor de MEDIA será exibido.
# O ponto (.) indica a precisão/número de casas decimais.
# 5f, o f irá indicar que a variável será formatada como um número de ponto flutuante (float), já o 5 indicará que o número será exibido com 5 casas decimais.