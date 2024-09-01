a, b, c, d = map(int, input().split())

if a > b:
    max1 = a
else:
    max1 = b

if c > d:
    max2 = c
else:
    max2 = d

print(int(max1+max2))