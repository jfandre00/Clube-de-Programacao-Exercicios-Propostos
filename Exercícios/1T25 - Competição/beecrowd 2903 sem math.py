def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

R = float(input())
R_int = int(round(R * 100))
gcd_val = gcd(36000, R_int)
N = 36000 // gcd_val
print(N)