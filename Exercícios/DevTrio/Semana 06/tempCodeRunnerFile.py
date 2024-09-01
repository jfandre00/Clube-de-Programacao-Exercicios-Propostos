N = int(input())
animal = list(map(int, input().split()))

if len(animal) % 2 == 0:
    print("YES")
else:
    print("NO")
    