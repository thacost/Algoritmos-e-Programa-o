# https://www.beecrowd.com.br/judge/pt/custom-runs/code/393928



plano = str(input())
salario_atual = float(input())
char = 'A';'B';'C'

if plano == 'A':
    salario = salario_atual + (salario_atual * 0.10)
    print(f"Novo salário: R${salario:.2f}")
elif plano == 'B':
    salario = salario_atual + (salario_atual * 0.15)
    print(f"Novo salário: R${salario:.2f}")
elif plano == 'C':
    salario = salario_atual + (salario_atual * 0.20)
    print(f"Novo salário: R${salario:.2f}")
