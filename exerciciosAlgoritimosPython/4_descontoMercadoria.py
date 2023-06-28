precoDaMercadoria = float(input('Informe o preço da mercadoria: '))
descontoPercentual = float(input('Informe percentual de desconto: '))

desconto = precoDaMercadoria * (descontoPercentual/100)
valorAtualMercadoria = precoDaMercadoria - desconto

print('O desconto será de R$ {:.2f}, e o valor agora é de R$ {:.2f}'.format(desconto,valorAtualMercadoria))