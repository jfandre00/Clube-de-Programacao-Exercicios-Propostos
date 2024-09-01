X, Y = map(int, input().split())
#X é o número de dias
#Y é o número de cápsulas

total_capsulas = 3*X
if total_capsulas > Y:
    print("NO")
else:
    print("YES")