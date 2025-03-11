def caminhos(n):
    if n < 0:
        return 0
    if n < 3:
        return n
    if n == 3:
        return 4
    return caminhos(n-1) + caminhos(n-2) + caminhos(n-3) 

print(caminhos(5)) # 13
#Como funciona a função caminhos(5)?
# caminhos(5) = caminhos(4) + caminhos(3) + caminhos(2)
# caminhos(4) = caminhos(3) + caminhos(2) + caminhos(1)
# caminhos(3) = 4
# caminhos(2) = 2
# caminhos(1) = 1
