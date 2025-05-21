# Você foi contratado pelas Indústrias Udilandenses (INUDIL) para desenvolver uma maneira de verificar se o Cadastro de Pessoa Física (CPF) indicado por um cliente era válido ou não. Conversando com amigos, você chegou à conclusão de que um CPF seria válido se a soma de todos os seus dígitos resultasse em número múltiplo de 11. Após verificação minuciosa, você descobriu que essa maneira só funciona em cerca de 80% dos casos, e você precisa de mais do que isso para garantir a qualidade do seu trabalho. Após pesquisar mais, você descobriu que dos 11 dígitos do CPF, os dois últimos são verificadores e dependem dos 9 dígitos anteriores. Vamos introduzir alguma notação. Considere um CPF com os seguintes dígitos
#
# a1a2a3.a4a5a6.a7a8a9-b1b2
# Para descobrirmos o dígito b1, procedemos da seguinte maneira: multiplicamos o primeiro por 1, o segundo por 2, o terceiro por 3, o quarto por 4 e vamos assim até multiplicarmos o nono por 9. Então, somamos tudo isto. Após termos somado tudo, dividimos por 11. O dígito b1 será o resto da divisão (ou 0, caso o resto seja 10).
#
# Para o segundo dígito verificador, temos o seguinte: multiplicamos o primeiro por 9, o segundo por 8, o terceiro por 7, o quarto por 6 e vamos assim até multiplicarmos o nono por 1. Então, somamos tudo isto e dividimos por 11. O dígito b2 será o resto da divisão (ou 0, caso o resto seja 10).
#
# Sabendo que isso vale para 100% dos CPFs, sua missão é implementar um programa que, dado um CPF, diga se ele é válido ou não.
#
# Entrada
# A entrada contém um número desconhecido de CPFs, que não excede 10000 casos. Em cada linha, um CPF na forma
#
# d1d2d3.d4d5d6.d7d8d9-d10d11
#
# Saída
# Se o CPF informado for válido, escreva "CPF valido". Caso contrário, escreva "CPF invalido".
#Exemplo de Entrada	             Exemplo de Saída
# 048.856.829-63                   CPF invalido
# 733.184.680-96                   CPF valido
# 227.518.471-08                   CPF invalido
# 092.844.842-86                   CPF valido
# 098.447.895-55                   CPF invalido

def cpf_valido(cpf_str):
    cpf_numeros = '' # Remove manualmente os caracteres '.' e '-'
    for c in cpf_str:
        if c != '.' and c != '-':
            cpf_numeros += c

    if len(cpf_numeros) != 11 or not cpf_numeros.isdigit(): # Verifica se há exatamente 11 dígitos e todos são numéricos
        return False

    # Separador de dígitos
    a = [int(cpf_numeros[i]) for i in range(9)]
    b1_esperado = int(cpf_numeros[9])
    b2_esperado = int(cpf_numeros[10])

    # Calculando b1
    soma_b1 = 0
    for i in range(9):
        soma_b1 += (i + 1) * a[i]
    b1 = soma_b1 % 11
    if b1 == 10:
        b1 = 0

    # Calculando b2
    soma_b2 = 0
    for i in range(9):
        soma_b2 += (9 - i) * a[i]
    b2 = soma_b2 % 11
    if b2 == 10:
        b2 = 0

    return b1 == b1_esperado and b2 == b2_esperado

# Lê CPFs até o fim da entrada
try:
    while True:
        linha = input().strip()
        if cpf_valido(linha):
            print("CPF valido")
        else:
            print("CPF invalido")
except EOFError:
    pass
