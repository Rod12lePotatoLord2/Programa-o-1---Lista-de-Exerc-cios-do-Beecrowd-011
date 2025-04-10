# Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".
#
# No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.
#
# Entrada
# A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.
#
# Saída
# Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema. Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error".

n1, n2, n3, n4 = map(float, input().split())

pesos = 2 + 3 + 4 + 1
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / pesos

print(f'Media: {media:.1f}')

if media >= 7:
    print('Aluno aprovado.')

elif 5 <= media <= 6.9:
    print('Aluno em exame.')
    nota = float(input())
    print(f'Nota do exame: {nota:.1f}')

    reajuste = (media + nota) / 2

    if reajuste >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(f'Media final: {reajuste:.1f}')
else:
    print('Aluno reprovado.')

# Os valores de n são digitados pelo usuário
# O map, juntamente do float converterá esses valores em pontos flutuantes (números com vírgula)
# O split dividirá a entrada em 4 partes diferentes
# Os pesos equivalem a soma dos pesos das notas (2, 3, 4 e 1), que são usados para ponderar cada uma das notas (totalizando 10)
# Media calculará a média ponderada das 4 notas inseridas, em seguida as multiplicará pelos seus respectivos pesos.
# Em seguidas elas serão divididas pela soma dos pesos (10)
# A média será impressa na tela
# O if irá verificar se a média calculada está acima de 7, se a resposta for verdadeira, a mensagem 'Aluno aprovado' será exibida
# Se a média estiver entre 5 e 6,9, a mensagem 'Aluno em exame' será exibida
# Em seguida a nota desse exame deverá ser digitada pelo usuário e então será exibida como um número flutuante com uma casa decimal
# A variável reajuste irá calular a antiga média com a nova nota e a dividirá por 2, gerando uma nova média
# Se essa média for igual ou maior do que 5, a mensagem 'Aluno aprovado' será exibida na tela
# Caso contrário, a mensagem 'Aluno reprovado' será exibida
# Por fim, a média final será impressa, determinando a situação do aluno