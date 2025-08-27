n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    if b > a:
        print("nao encaixa")
        continue
    else:
        str_a = str(a)
        str_b = str(b)
        if str_a[-len(str_b):] == str_b:
            print("encaixa")
        else:
            print("nao encaixa")
