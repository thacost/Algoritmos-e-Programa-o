# https://www.beecrowd.com.br/judge/pt/custom-runs/code/393923



tipo_cliente = int(input())
valor_total = float(input())

if tipo_cliente == 1:
    valor = valor_total
    print(f"Valor total a ser pago: R${valor:.2f}")
elif tipo_cliente == 2:
    valor = valor_total - (valor_total * 0.13)
    print(f"Valor total a ser pago: R${valor:.2f}")
elif tipo_cliente == 3:
    valor = valor_total - (valor_total * 0.07)
    print(f"Valor total a ser pago: R${valor:.2f}")
else:
    print("OPÇÃO INVÁLIDA!")