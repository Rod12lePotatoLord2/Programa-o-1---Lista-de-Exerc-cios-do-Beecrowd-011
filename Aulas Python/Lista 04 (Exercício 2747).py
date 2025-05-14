# O seu professor de programação gostaria de fazer uma tela com as seguintes características:
# 
# Ter 39 traços (-) na primeira linha;
# Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira linha, preencher no meio com espaço em branco;
# Repita o procedimento 2 mais quatro vezes;
# Repita o procedimento 1.
# No final deve ficar igual a imagem a seguir:
# 
# --------------------------------------- (39 traços)
# |                                     |
# |                                     |
# |                                     |
# |                                     |
# |                                     |
# --------------------------------------- (39 traços)
# Entrada              Saída
# Não há.             A saída será impressa conforme a figura acima.

def gerador_de_tracos():
    # Imprime a fileira do topo
    print('-' * 39)
    # Imprime 5 fileiras de barras verticais com espaços entre elas
    for _ in range(5):
        print('|' + ' ' * 37 + '|')
    # Imprime a fileira final
    print('-' * 39)


# Chama a função para ser gerada na tela
gerador_de_tracos()