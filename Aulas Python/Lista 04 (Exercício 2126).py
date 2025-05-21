# Dados dois números naturais N1 e N2, diz-se que N1 é subsequência contígua de N2 se todos os dígitos de N1 aparecem, na mesma ordem e de forma contígua, em N2. Crie uma aplicação que leia dois números naturais e diga se o primeiro é uma subsequência contígua do segundo.
#
# Entrada
# A entrada é composta por vários casos de teste e termina com final de arquivo (EOF). A primeira linha de cada entrada é composta por um valor natural N1(1 < N1 < 1010), a segunda linha é composta por um valor N2( N1 < N2 < 10^32).
#
# Saída
# Para cada caso de teste imprima a quantidade de subsequências contíguas e a posição onde a subsequência é iniciada, caso exista mais de uma subsequência, imprima onde é iniciada a última subsequência. Caso não exista subsequência, imprima "Nao existe subsequencia". Mostre o resultado conforme o exemplo de saída.

# Exemplos de Entrada                   Exemplos de Saída
# 78954                                     Caso #1:
# 7895478954789547895447895478954       Qtd.Subsequencias: 6
#                                           Pos: 27
#
# 464133                                  Caso #2:
# 1331646546874694                     Nao existe subsequencia
#
# 12                                        Caso #3:
# 1231321455123214565423112            Qtd.Subsequencias: 3
#                                           Pos: 24

caso = 1 # Inicia o contador para numerar os casos.
while True: # Laço infinito que só para com break.
    try: # Permite que o programa leia entradas até que o fim do arquivo (EOF) seja alcançado.
        n1 = input()
        n2 = input()
        print('Caso #%d:' % caso)
        qt = n2.count(n1)
        if qt == 0:
            print('Nao existe subsequencia')
        else:
            print('Qtd.Subsequencias: %d' % qt)
            qt = n2.rfind(n1)
            print('Pos: %d' % (int(qt) + 1))
        print()
        caso += 1

    except EOFError: # Ao alcançar o EOF, o programa encerra com break
        break