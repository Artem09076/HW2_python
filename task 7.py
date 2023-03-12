n = int(input())
s = 0
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        s += 1
    elif n // i != i:
        s += 1

print(s)
