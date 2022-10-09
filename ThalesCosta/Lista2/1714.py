# https://www.beecrowd.com.br/judge/pt/custom-runs/code/393836



compra = float(input())
if compra < 20:
    print(f'Valor de venda:R${compra * 1.45:.2f}')
else:
    print(f'Valor de venda:R${compra * 1.3:.2f}')