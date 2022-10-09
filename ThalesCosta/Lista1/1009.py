# https://www.beecrowd.com.br/judge/pt/runs/code/29443201



nome = input()
salariofixo = float(input())
quantidadedevendas = float(input())

bonus = float(quantidadedevendas * (15/100))

total = salariofixo + bonus

print("TOTAL = R$ %0.2f" %total)