# A cifra mais antiga conhecida é a Cifra de César. César escrevia suas cartas trocando cada letra pela próxima do alfabeto, para evitar que, quando a carta fosse interceptada, conseguissem ler. Com o tempo, a criptografia adquiriu melhor qualidade, mas a criptografia por substituição ainda é uma brincadeira de criança interessante, por exemplo:

# ZEN I T
# POLAR

# Neste tipo de brincadeira, ao escrever uma carta a letra Z é trocada pela letra P e vice versa, bem como: E e O e assim sucessivamente. A frase cifrada desta forma: "Osro roxre osri caftide" pode ser decifrada como: "Este texto esta cifrado". Como a brincadeira ficou séria, a você foi solicitado um programa que decifre as mensagens cifradas a partir de uma chave fornecida.

# Entrada
# A entrada contém vários casos de teste. Cada caso de teste começa com uma linha indicando dois números inteiros C e N, 0 < C < 21 e 0 < N < 100. C é o tamanho da cifra. Nas duas linhas seguintes está a cifra de tamanho C indicando quais caracteres da primeira linha será substituído por caracteres da segunda linha, um caracter aparece uma única vez, na primeira ou na segunda linha.

# A cifra pode conter letras de ‘A’ a ‘Z’, números de ‘0’ a ‘9’ além do espaço em branco e alguns símbolos de pontuação: '.' ',' ';' ':' '(' ')' '!' e '?'. Nas próximas N linhas estão frases e sentenças criptografadas pela cifra fornecida, que você deve decifrar. Cada linha contém no mínimo 1 e no máximo 1000 caracteres. São permitidos quaisquer caracteres ASCII (não extendido) imprimíveis, neste caso não estão presentes nenhum caracter acentuado, nem mesmo 'ç'.

# Saída
# Para cada caso de teste da entrada seu programa deve gerar para cada linha de frase e sentença de entrada, uma linha com a saída decifrada, respeitando a capitalização da letra (letras maiúsculas são decifradas como maiúsculas e minúsculas como minúsculas quando for possível aplicar a diferenciação, se não for possível serão decifrados como letras minúsculas). Após cada caso de teste deve ser impressa uma linha em branco, inclusive após o último.

# Exemplo de Entrada	                                                Exemplo de Saída
# 5 3
# ZENIT
# POLAR
# Osro roxre osri caftide                                               Este texto esta cifrado
# Osri o umi roclaci do ctazregtifai zet subsraruacie                   Esta e uma tecnica de criptografia por substituicao
# Zedo sot ficanmolro quobtide i zitrat do umi bei imesrti do roxre     Pode ser facilmente quebrado a partir de uma boa amostra de texto

# 3 2
# UMA
# 123
# C3d3 12 por si                                                        Cada um por si
# 123 3 123                                                             uma a uma

while True:
    try:
        # Lê o tamanho da cifra e o número de mensagens
        c, n = map(int, input().split())
        linha1 = input().strip()
        linha2 = input().strip()

        # Cria dicionário de mapeamento direto e reverso (case insensitive)
        mapa = {}

        for ch1, ch2 in zip(linha1, linha2):
            mapa[ch1.lower()] = ch2.lower()
            mapa[ch2.lower()] = ch1.lower()

        for _ in range(n):
            mensagem = input().strip()
            resultado = []

            for ch in mensagem:
                ch_lower = ch.lower()
                if ch_lower in mapa:
                    subst = mapa[ch_lower]
                    if ch.isupper():
                        resultado.append(subst.upper())
                    else:
                        resultado.append(subst)
                else:
                    resultado.append(ch)

            print(''.join(resultado))

        print()  # Linha em branco após cada caso de teste

    except EOFError:
        break

# O loop while True roda indefinidamente até que ocorra um EOFError, ou seja, até que não haja mais entrada a ser lida (fim do arquivo/entrada).
# Isso permite processar múltiplos casos de teste consecutivos.
# c é o tamanho do alfabeto da cifra (número de letras mapeadas).
# n é o número de mensagens que precisam ser decifradas.
# linha1 e linha2 são dois alfabetos de mesmo tamanho, indicando a substituição entre as letras: letra em linha1[i] é substituída por linha2[i], e vice-versa.
# O mapa é um dicionário que armazena a substituição bidirecional (de linha1 para linha2 e vice-versa).
# Usa .lower() para tornar a substituição case insensitive, ou seja, trata letras maiúsculas e minúsculas da mesma forma.
# No for.Para cada uma das n mensagens:
# Substitui letra por letra usando o mapa criado.
# Preserva a capitalização original (ch.isupper()).
# Caracteres que não estão no mapa (Pontuação, espaços, números) são mantidos como estão.
# Após processar todas as mensagens de um caso de teste, imprime uma linha em branco para separá-lo do próximo.
# Em resumo:
# O código é um decodificador de cifra por substituição, com as seguintes características:
# Substituição bidirecional (de linha1 para linha2 e vice-versa).
# Sensível a maiúsculas/minúsculas (preserva a forma original).
# Roda até o fim da entrada (EOF).