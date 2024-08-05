entrada = input()
A, B, C = map(int, entrada.split())

maiorAB =  (A + B + abs(A-B))/2

maiorABC = (maiorAB + C + abs(maiorAB-C))/2

print(f'{maiorABC:.0f} eh o maior')
