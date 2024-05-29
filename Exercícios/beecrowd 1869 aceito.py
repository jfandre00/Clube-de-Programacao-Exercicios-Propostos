b = []
for i in range(32):
    if(i<10):
        b.append(i)
    else:
        b.append(chr(i+55))
#Acima criou a lista de base 32, de 0 a 9 e de A a V

while(True):
    n = int(input())
    ans = ''
    while(n > 31):
        i = int(n%32)
        ans += str(b[i])
        n /= 32
    ans += str(b[int(n)])
    ans = ans[::-1]
    print(ans)
    if(n == 0):
        break