# легкий
a = [int(x) for x in open("17.txt")]
def dell(n):
    return sorted({x for d in range(2, int(n ** 0.5) + 1) if n % d == 0 for x in (d, n // d)})
k = 0
ms = 0
for i in range(len(a) - 1):
    if len(dell(a[i])) == len(dell(a[i + 1])):
        k += 1
        ms = max(ms, a[i] + a[i + 1])
print(k, ms)
# cредний
a = [int(x) for x in open("17.txt")]
k = 0
ms = 0
def dell(n):
    return sorted({x for d in range(2, int(n ** 0.5) + 1) if n % d == 0 for x in (d, n // d)})
def prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))
for i in range(len(a) - 1):
    del1 = [x for x in dell(a[i]) if prime(x)]
    del2 = [x for x in dell(a[i + 1]) if prime(x)]
    if len(del1) == len(del2):
        k += 1
        ms = max(ms, a[i] + a[i + 1])
print(k, ms)
# Сложный
a = [int(x) for x in open("17.txt")]
k = 0
ms = 0
k3 = 0
def dell(n):
    return sorted({x for d in range(2, int(n ** 0.5) + 1) if n % d == 0 for x in (d, n // d)})
def prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))
for i in range(len(a) - 1):
    del1 = [x for x in dell(a[i]) if prime(x)]
    del2 = [x for x in dell(a[i + 1]) if prime(x)]
    kd = 0
    for d1 in del1:
        for d2 in del2:
            if d1 == d2:
                kd += 1
    if kd < 3:
        k += 1
        ms = max(ms, a[i] + a[i + 1])
print(k, ms)
