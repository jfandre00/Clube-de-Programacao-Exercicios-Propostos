import math

n = int(input())
while n > 0:
    cerca = input().split()
    postes = 0
    bons = [i for i in range(n) if cerca [i] == "1"]
    if len(bons) > 0:
        for i in range(len(bons) - 1):
            dist = bons[i +1] - bons[i]
            postes += (dist - 1) // 2
        dist = n - bons[-1] + bons[0]
        postes += (dist -1) // 2
    else:
        postes += math.ceil(n/2)
    print(postes)
    n = int(input())