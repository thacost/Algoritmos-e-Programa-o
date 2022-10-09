# https://www.beecrowd.com.br/judge/pt/custom-runs/code/395742


n = int(input())
x = n
f = 1
while x > 0:
    f = f * x
    x = x - 1
print("%i! = %i" %(n ,f))