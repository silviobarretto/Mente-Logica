# Uma loja oferece um desconto se o cliente comprar mais de 10 itens ou se o
# valor total da compra for superior a R$100.
# Dados:
# Quantidade de itens: 8
# Valor total: R$120
# Verifique se o cliente tem direito ao desconto.

qtdeItens = 8
valorTotal = 120.00

desconto = (qtdeItens >= 10) or (valorTotal >= 100.00)

print('Cliente tem direito ao desconto?', desconto)
