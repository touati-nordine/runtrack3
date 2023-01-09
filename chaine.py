chaine = "abcdefghijklmnopqrstuvwxyz" * 10

l = len(chaine)
n = 1
while True:
    if n * (n + 1) // 2 > l:
        break
    n += 1
n -= 1

for i in range(n):
    print(chaine[i * (i + 1) // 2: (i + 1) * (i + 2) // 2])
