# -*- coding: utf-8 -*-

n = int(input()) #quantidade de leituras


for _ in range(n):
    x = int(input())
    if x == 0:
        print("NULL")
        continue
    if x > 0:
        tipo = "POSITIVE"
    else:
        tipo = "NEGATIVE"
    if x % 2 == 0:
        par_impar = "EVEN"
    else:
        par_impar = "ODD"
    
    print(f"{par_impar} {tipo}")