# https://www.beecrowd.com.br/judge/pt/custom-runs/code/395794


n = str(input())
ht = float(input())
salariomin = (1192.40)
he = (10.00)

salarioextra = ht * he
salariobruto = salarioextra + (3 * salariomin)

if(salariobruto > 2000):
    inss = salariobruto * 0.12
else:
    inss = salariobruto * 0.05

if(salariobruto > 2500):
    ir = salariobruto * 0.20
else:
    ir = salariobruto

descontos = inss + ir
salarioliq = salariobruto - descontos

print(f"Nome: {n}\nSalário bruto: R${salariobruto:.2f}\nSalário líquido: R${salarioliq:.2f}")