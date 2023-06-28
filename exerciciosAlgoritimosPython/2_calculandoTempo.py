dias = input('Insira os dias: ')
horas = input('Insira as horas: ')
minutos = input('Insira os minutos: ')
segundos = input('Insira os segundos: ')

convertendoEmSegundos = (float(dias) * 24 * 60 * 60) + (float(horas)* 60 * 60) + (float(minutos) * 60) + (float(segundos))

print('Os segundos são: ',convertendoEmSegundos)