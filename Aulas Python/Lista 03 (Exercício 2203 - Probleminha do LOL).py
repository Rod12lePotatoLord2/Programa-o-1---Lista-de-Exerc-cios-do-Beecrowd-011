# Fiddlesticks é um campeão do jogo League of Legends e tem como sua habilidade ultimate a "Tempestade de Corvos", ela funciona da seguinte maneira:

# Primeiro Fiddlesticks escolhe um local estratégico e prontamente ele se prepara para ressurgir em uma direção até uma certa distância, então ele se enraiza e canaliza a ultimate por exatamente 1.5 segundos, após esse tempo ele ressurge imediatamente no local alvo com uma revoada de corvos voando ao seu redor e causando muito dano.

# Fiddlesticks quer sua ajuda para saber se de uma certa posição é possível atingir um invasor com sua habilidade ultimate.

# Obs: Considere que Fiddlesticks sempre luta exatamente na direção do invasor e o invasor sempre tenta fugir na direção contrária a Fiddlesticks, em velocidade constante.

# Entrada
# A entrada é composta de várias linhas, cada linha contém os seguintes valores inteiros: Xf, Yf, Xi, Yi, Vi, R1 e R2(0 ≤ Xf, Yf, Xi, Yi, Vi, R1 e R2 ≤ 100), representando respectivamente as coordenadas de Fiddlesticks, as coordenadas iniciais do invasor, a velocidade do invasor, o raio de conjuração da ultimate e o raio de voo dos corvos. Considere a unidade de medida como sendo o metro.
# 
# Saída
# Na saída você deve imprimir para cada linha o caractere 'Y' caso seja possível atingir o invasor ou 'N' caso contrário, ambos seguidos de uma quebra de linha.

while True:
    try:
        Xf, Yf, Xi, Yi, Vi, R1, R2 = map(int, input().split())
        dx = Xi - Xf
        dy = Yi - Yf
        distancia_inicial = (dx * dx + dy * dy) ** 0.5
        distancia_da_movimentacao = Vi * 1.5
        distancia_total = distancia_inicial + distancia_da_movimentacao
        alcance = R1 + R2
        if distancia_total <= alcance:
            print('Y')
        else:
            print('N')
    except EOFError:
        break

# O loop while True vai manter o programa rodando indefinidamente, até que uma exceção de fim de entrada (EOF) ocorra.
# EOF é um sinalizador que indica que não há mais dados para serem lidos.
# A parte do try tenta executar o bloco de código até que não haja mais entrada (por exemplo, ao ler de um arquivo ou do terminal com redirecionamento).
# Quando não houver mais dados, sai do loop (break)
# Um EOFError ocorre quando uma função interna, tenta ler além do final do arquivo ou fluxo de entrada
# A linha de Xf contém 7 números inteiros digitados pelo usuário sendo eles:
# Xf, Yf: Coordenadas do alvo fixo.
# Xi, Yi: Coordenadas do ponto de origem.
# Vi: velocidade da movimentação.
# R1, R2: raios dos dois objetos (ou zonas de alcance).
# A distância entre os pontos Xi, Yi e Xf, Yf será calculada usando a fórmula da distância euclidiana.
# A variável distancia_da_movimentacao calcula quanto o personagem pode se mover em 1.5 segundos
# A distancia_total soma a distância inicial com a que o personagem pode se mover (a distância máxima que pode alcançar).
# A condicional if vai verificar se a distância total (do personagem até o alvo, considerando o movimento) é menor ou igual à soma dos raios.
# Se sim, imprime Y (atinge o alvo).
# Caso contrário, imprime N (não atinge o alvo)