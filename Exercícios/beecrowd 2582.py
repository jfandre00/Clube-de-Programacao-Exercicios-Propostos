valores = input().split()

val1 = int(valores[0])
val2 = int(valores[1])

musica = val1 + val2
lista = ['PROXYCITY','P.Y.N.G.','DNSUEY!','SERVERS','HOST!','CRIPTONIZE','OFFLINE DAY', 'SALT','ANSWER!','RAR?','WIFI ANTENNAS']

print(lista[musica])

# outra solução 
'''song = ['PROXYCITY','P.Y.N.G.','DNSUEY!','SERVERS','HOST!','CRIPTONIZE','OFFLINE DAY', 'SALT','ANSWER!','RAR?','WIFI ANTENNAS']
n = int(input())
while(n>0):
    n -= 1
    x, y = input().split()
    print(song[int(x)+int(y)])'''