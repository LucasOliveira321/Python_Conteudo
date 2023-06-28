from ctypes.wintypes import PINT


salarioAtual = float(input('Informe seu salário atual: '))
aumento = float(input('Informe seu ajuste salárial em porcentagem: '))

ajuste = salarioAtual + (salarioAtual*(aumento/100))

print('Seu salário agora é R$',ajuste)