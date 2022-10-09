# https://www.beecrowd.com.br/judge/pt/custom-runs/code/404496



total = 0


while True:
    valor_compra = float(input())
    total += valor_compra
    if valor_compra == 0:
        valor_pago = float(input(''))
        break
print('Total da compra: R$%.2f' %total)
print('Valor pago: R$%.2f'%valor_pago)
troco = valor_pago - total
print('Troco: R$%.2f'%troco)