# Resolvendo usando recursão

def frac_continua(n):
    if n == 0:
        return 0
    return 1 / (2 + frac_continua(n - 1))

N = int(input())
resultado = 1 + frac_continua(N)
print(f"{resultado:.10f}")
