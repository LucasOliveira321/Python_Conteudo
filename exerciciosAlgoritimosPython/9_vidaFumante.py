# Quantidade de cigarros fumados por dia, quantos anos já fumou,perde 10 minutos de vida em cada cigarro
# Exibir em total de dias

cigarrosDia = int(input('Informe quantos cigarros em média você fuma por dia: '))
tempoFumando = float(input('Informe quantos anos você está fumando: '))

tempoPerdido = ((cigarrosDia * (tempoFumando*365)) * 10) / 1440

print('Você reduziu {:.2f} dias de sua vida!'.format(tempoPerdido))