# https://www.beecrowd.com.br/judge/pt/custom-runs/code/404494

ano_atual = int(input())
valor_inicial = 1015
valor_somado = 1015
contadorPorc = 0.015
somaPorc = 0.01

anos = ano_atual - 2006

if ano_atual < 2006:
    print("O ano informado deverá ser > 2005!")

elif ano_atual == 2006:
    print("Salário atual: R$%.2f" %(valor_inicial))

elif ano_atual > 2006:
    porcentagem = (0.015 + 0.01)
    ant = valor_inicial

    for x in range(anos):
        calculo = ant + (ant * porcentagem)
        ant = calculo
        porcentagem += 0.01
        
    print("Salário atual: R$%.2f"%(calculo))