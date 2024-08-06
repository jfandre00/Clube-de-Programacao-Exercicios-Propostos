def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    while True:
        n = int(data[index])
        index += 1
        if n == 0:
            break
        
        zero = 0
        soma = 0
        inicio = 0
        postes = 0
        
        for _ in range(n):
            numero = int(data[index])
            index += 1
            if numero == 0 and inicio == 0:
                zero += 1
                postes += 1
            elif numero == 0 and inicio == 1:
                postes += 1
            if numero == 1:
                inicio = 1
                soma += postes // 2
                postes = 0
        
        if postes > 0:
            soma -= zero // 2
            postes += zero
            soma += postes // 2
        
        print(soma)

if __name__ == "__main__":
    main()