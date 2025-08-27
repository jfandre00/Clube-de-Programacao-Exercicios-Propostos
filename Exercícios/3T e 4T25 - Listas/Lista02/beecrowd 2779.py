n = int(input()) #quantas figurinhas tem o album no total
m = int(input()) #quantas figurinhas foram compradas
set_figurinhas = set() #conjunto para armazenar as figurinhas compradas

for _ in range(m):
    x = int(input()) #figurinhas compradas
    set_figurinhas.add(x) #adiciona a figurinha ao conjunto

quantas_figurinhas_faltam = n - len(set_figurinhas) 

print(quantas_figurinhas_faltam)
