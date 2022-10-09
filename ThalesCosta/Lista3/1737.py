# https://www.beecrowd.com.br/judge/pt/custom-runs/code/397999


n = int(input())

if n > 0:
        contador = 0
        soma = 0
        while contador < n:
                n1 = float(input())
                soma = soma + n1
                contador = contador + 1
        print(f"Soma dos números informados: {soma:.2f}")
else:
        print("Informe uma quantidade >0!")