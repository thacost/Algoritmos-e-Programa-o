# https://www.beecrowd.com.br/judge/pt/custom-runs/code/393834



vh = float(input())
vt = float(input())
salario_bruto = vh * vt
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sind = salario_bruto * 0.05
liq =  salario_bruto - (ir + inss + sind)

print(f"Salário bruto: R${salario_bruto:.2f}")
print(f"Imposto: R${ir:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"Sindicato: R${sind:.2f}")
print(f"Líquido: R${liq:.2f}")