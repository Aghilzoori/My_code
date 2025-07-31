vorodi = int(input())

n = vorodi
faktor = 1
zakhire = []
while n > 0:
    faktor *= n
    zakhire.append(str(n))
    n -= 1
print(f"{n}!:{'*'.join(zakhire)} = {faktor}")