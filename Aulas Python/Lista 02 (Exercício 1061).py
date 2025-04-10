# Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

# Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

# Entrada
# Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

# Saída
# Na saída, deve ser apresentada a duração do evento, no seguinte formato:

# W dia(s)
# X hora(s)
# Y minuto(s)
# Z segundo(s)

# Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

dia_inicial_do_evento = int(input().split()[1])
hh, mm, ss = map(int, input().strip().split(' : '))

dia_final_do_evento = int(input().split()[1])
hora, minuto, segundo = map(int, input().strip().split(' : '))

inicio_em_segundos = (dia_inicial_do_evento * 86400) + (hh * 3600) + (mm * 60) + ss
fim_em_segundos = (dia_final_do_evento * 86400) + (hora * 3600) + (minuto * 60) + segundo

duracao_total_do_evento = fim_em_segundos - inicio_em_segundos

if duracao_total_do_evento < 60:
    duracao_total_do_evento = 60

dias_do_evento = duracao_total_do_evento // 86400
duracao_total_do_evento %= 86400

horas_do_evento = duracao_total_do_evento // 3600
duracao_total_do_evento %= 3600

minutos_do_evento = duracao_total_do_evento // 60

segundos_do_evento = duracao_total_do_evento % 60

print(f'{dias_do_evento} dia(s)')
print(f'{horas_do_evento} hora(s)')
print(f'{minutos_do_evento} minuto(s)')
print(f'{segundos_do_evento} segundo(s)')

# A entrada dia_inicial_do_evento representa a data inicial no formato Dia
# A função input().split()[1] vai ler a entrada e dividir a string usando espaços, pegando a parte que está na primeira posição (Ou seja: O dia)
# A entrada hh, mm, ss representa a hora de início do evento no formato Hora:Minuto:Segundo
# A função strip() vai remover os espaços em branco desnecessários nas extremidades da linha
# O split irá dividirá a string em 3 partes usando ":" como separador
# O map(int, input() irá converter as partes inseridas em valores inteiros para representar horas, minutos e segundos
# O mesmo processo é válido para as variável dia_final_do_evento só que referente ao último dia do evento
# inicio_em_segundos irá transformar o tempo do evento em segundos.
# O número de dias é multiplicado por 86400 (número de segundos em um dia), as horas por 3600 (segundos em uma hora), os minutos por 60 (segundos em um minuto)
# Então, os segundos são somados.
# O mesmo é feito para o tempo final fim_em_segundos
# duracao_total_do_evento irá calcular a diferença entre o ínicio e o fim do evento em segundos
# A condicional if servirá para verificar se o evento durou menos de 1 minuto, então ajustará a duração mínima para 60 segundos
# A variável dias_do_evento irá fazer a divisão inteira do valor de duracao_total_do_evento por 86400 (Total de segundos em um dia), resultando no número de dias
# %= Atualizará o valor de duracao_total_do_evento para que o resto das conversões possa ser feita
# A variável horas_do_evento fará a divisão inteira de duracao_total_do_evento por 3600 (Total de segundos em uma hora), resultando no número de horas.
# O valor será novamente atualizado
# O mesmo ocorre para minutos_do_evento e segundos_do_evento
# Por fim, o print servirá para imprimir a duração do evento em dias, horas, minutos e segundos