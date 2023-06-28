# calcule o preço a pagar, sabendo que o carro R$60,00 por dia e R$0,15 por km rodado

diasAluguel = int(input('Informe os dias completos que irá utilizar o carro: '))
kmRodado = float(input('Informe o km de deseja contratar: '))

vlrCobrado = (diasAluguel * 60) + (kmRodado * 0.15)

print('O custo do aluguel será de R$ {:.2f}.'.format(vlrCobrado))